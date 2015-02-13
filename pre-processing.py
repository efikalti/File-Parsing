import sys, getopt
from unidecode import unidecode
import codecs

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'usage: test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print 'Input file is', inputfile
   print 'Output file is', outputfile

   str = raw_input("press enter to continue: ");
   if str=="":
        print "good lets continue"
        infile = codecs.open(inputfile,encoding='utf-8',mode='r')
        for line in infile:
            line = unidecode(line)
            line.lower()
            print line
   else:
        exit(0)

if __name__ == "__main__":
   main(sys.argv[1:])