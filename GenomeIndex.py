
import re
''' This class contains genomic coordinates chromosome, start position, and CIGAR string'''
class GenomicCoordinates:

    # adding chr #
    def addCr(self,cr):
        self.cr = cr

    # adding chromosome index. crIndex refers to the start position of the transcript on thh reference genome#
    def addCrIndex(self,cr_index):
        self.cr_index = cr_index

    # adding CIGAR string #
    def addCigar(self,cigar):
        self.cigar = cigar

    ''' parse the CIGAR string by type of operator and length of each operator.CIGAR has 8 different operators
    M - match or mismatch 
    X = mismatch 
    = - match 
    D - deletion 
    N - skipped 
    I - insertion 
    S - soft clipping
    H - hard clipping  
    The index of transcript and the reference genome starts from 0 coordinate
    If cigar type is M (match/mismatch), X (i.emismmatch), or = (i.e perfect match), increment the index.
    The coordinate of transcript (i.e query) is skipped if the cigar operation is D deletion or N 
    The gene coordinate is provided as None if cigar type is I, S, or H'''

    def parse(self,types,positions,start):
        self.d = {}
        read_pos = 0
        
        for i in range(len(types)):
            t,p = types[i],int(positions[i])
            if(t == 'M' or t == 'X' or t == '='):
                while(p > 0):
                    self.d[read_pos] = start
                    read_pos += 1
                    start += 1
                    p -= 1          
            elif(t == 'D' or t == 'N'):
                start += p
            else:
                while(p > 0):
                    self.d[read_pos] = None
                    read_pos += 1
                    p -= 1

######################### END OF CLASS ########################################################################

'''
 1. takes 3 input arguments input file path, query file patha, and output file path (if output file path doesn't exist then it creates the output in the given path)
 2. read the input file, parse the cigar string, and generates a dictionary (which is self.d in the above class) of transcript and gene coordinates
 3. reads the query text and finds the gene coordinate from the dictionary and writes to the output file  
 '''
def processor():
    try:
        inputfile_path,queryfile_path,outputfile_path=input("Enter Complete Path to Input File, Query File and Output File (separate them with spaces) :").split()
        print(f"The inputfile path : {inputfile_path}\nThe queryfile path : {queryfile_path}\nThe outputfile path : {outputfile_path}") 
        inputfile = open(f"{inputfile_path}","r")
        queryfile = open(f"{queryfile_path}","r")
        outputfile = open(f"{outputfile_path}","w")
        inputlines = inputfile.readlines()
        inputlines = filter(lambda line: not line.isspace(), inputlines)
        inputfile.close()

        dictOfGCoordinates = {}

        for inputline in inputlines:
            properties = inputline.split()
            gCoordinate = GenomicCoordinates()
            tr = ""
            for index in range(len(properties)):
                if index == 0:
                    tr = properties[index]
                elif index == 1:
                    gCoordinate.addCr(properties[index])
                elif index == 2:
                    gCoordinate.addCrIndex(properties[index])
                else:
                    gCoordinate.addCigar(properties[index])
            dictOfGCoordinates[tr] = gCoordinate
            types = re.split(r'\d+',gCoordinate.cigar)
            types = types[1:]
            positions = re.split(r'[A-Z]',gCoordinate.cigar)
            positions = positions[0:len(positions) - 1]
            gCoordinate.parse(types=types,positions=positions,start=int(gCoordinate.cr_index))



        querylines = queryfile.readlines()
        querylines = filter(lambda line: not line.isspace(), querylines)
        queryfile.close()

        for queryline in querylines:
            query = queryline.split()
            for index in range(len(query)):
                if index == 0:
                    trans = query[index]
                else:
                    tr_coordinate = query[index]
            cr_coordinate = dictOfGCoordinates[trans].d[int(tr_coordinate)]
            cr = dictOfGCoordinates[trans].cr
            outputfile.write(f"{trans} {tr_coordinate} {cr} {cr_coordinate}\n")
        outputfile.close()


    except KeyError:
        print("The transcript read coordinate is out of bound")
    except ValueError:
        print("Please check your input")
        raise
    except:
        raise