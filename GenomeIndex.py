class GenomicCoordinates:
    def addCr(self,cr):
        self.cr = cr
    def addCrIndex(self,cr_index):
        self.cr_index = cr_index
    def addCigar(self,cigar):
        self.cigar = cigar
    
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
    
import re
try:
    inputfile_path,queryfile_path,outputfile_path = input("Enter Complete Path to Input File, Query File and Output File (separate them with spaces) :").split()
    print(f"The inputfile path : {inputfile_path}\nThe queryfile path : {queryfile_path}\nThe outputfile path : {outputfile_path}")
    inputfile = open(f"{inputfile_path}","r")
    queryfile = open(f"{queryfile_path}","r")
    outputfile = open(f"{outputfile_path}","w")
    inputlines = inputfile.readlines()
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
    queryfile.close()

    
    
    for queryline in querylines:
        query = queryline.split()
        trans,tr_coordinate = query[0],query[1]
        cr_coordinate = dictOfGCoordinates[trans].d[int(tr_coordinate)]
        cr = dictOfGCoordinates[trans].cr
        outputfile.write(f"{trans} {tr_coordinate} {cr} {cr_coordinate}\n")
    outputfile.close()
except:
    print("There is an error while processing your input, please check your input paths.")