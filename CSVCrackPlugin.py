import sys

class CSVCrackPlugin:
    def input(self, inputfile):
        self.infile = open(inputfile, 'r')

    def run(self):
        pass

    def output(self, outputfile):
        outfile = open(outputfile, 'w')
        self.infile.readline()
        for line in self.infile:
            contents = line.strip().split(',')
            for i in range(1,len(contents)):
                outfile.write(contents[i])
                if (i != len(contents)-1):
                    outfile.write(',')
                else:
                    outfile.write('\n')

