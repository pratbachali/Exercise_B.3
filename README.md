# Exercise_B.3
The project is to trasnlate the transcript coordinates to the genome coordinates

1. This project has two files 
    i. GenomeIndex.py 
    ii. Testing.py

2. The project can be run with GenomeIndex.py by passing 3 arguments (input filepath, query filepath, output filepath)
3. Testing.py has two test validating the lengths and the content of the output text file.
4. A folder of testfiles is uploaded which was used for the development
        i.input.txt - Input file with transcript and genome coordinates (chromosome, transcript possition to the reference genome, CIGAR)
        ii.query.txt - Query file with transcript and transcript coordinate
        iii.output.txt - Output file which has the query ids and its respective mapped gene coordiantes
        iv. expected.txt - Expected text file submitted for the testing  


Assumptions 
1. The coordinate of transcript (i.e query) is skipped if the cigar operation is D deletion or N 
2. If the cigar operation type is I, S, or H, then the coordinate of reference genome is not present and hence the program maps it to 'None'. 
3. If cigar type is M (match/mismatch), X (i.emismmatch), or = (i.e perfect match), increment the index.
4. If the co-ordinate requested for transcript in the query is beyond the length of the transcript, then an exception "KeyError" is caught. The program still read such value and throws an exception.


Strengths:
1. All the co-ordinates of the transcript are mapped to a corresponding genome (from the given start position). A dictionary is used for the mapping. When a query text file is read, a transcript co-ordinate can be passed in to the dictionary and retrieve mapped genome co-ordinate. This is a O(1) time complexity operation, as retrieving from a dictionary can be done in constant time.

Weakness:
1. Since we are mapping  all the transcript co-ordinates with genome co-ordinates, this could be time consuming if the cigar string is big or if the cigar string has high number of matches (M) or inserts (I). For eg: if the transcript co-ordinate in the query is some where close to 0 or 0, then we still would have to parse entire CIGAR string. 


