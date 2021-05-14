import GenomeIndex
import unittest


class TestOutputMethods(unittest.TestCase):    
    
    GenomeIndex.processor()


    # Provide a path to read an expected  file
    expectedfile = open(r'/Users/prat/Documents/TestFiles/expected.txt',"r")
    expectedlines = expectedfile.readlines()
    explength = len(expectedfile.readlines())
    expectedlines = filter(lambda line: not line.isspace(), expectedlines)
    expectedfile.close()

    # Provide a path to read an output file
    outputfile = open(r'/Users/prat/Documents/TestFiles/output.txt',"r")
    ouputlines = outputfile.readlines()
    outlength = len(outputfile.readlines())
    ouputlines = filter(lambda line: not line.isspace(), ouputlines)
    outputfile.close()

    # This test is to validate the size of the output file
    def test_outputlength(self):    
        self.assertEqual(self.explength,self.outlength)
        
    # This test is to compare each line of the output file
    def test_output(self):
        for expline,outline in zip(self.expectedlines,self.ouputlines):
            for e,o in zip(expline,outline):
                self.assertEqual(e,o)
            

if __name__ == '__main__':
    unittest.main()

    

