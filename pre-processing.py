import sys, getopt
from unidecode import unidecode
import codecs
import re, string

def main(argv):
   inputfile = ''
   outputfile = ''
   reg_ex = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:r",["ifile=","ofile=","reg_ex="])
   except getopt.GetoptError:
      print 'usage: test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
      elif opt in ("-r", "--regex"):
          reg_ex = arg
   print 'Input file is', inputfile
   print 'Output file is', outputfile
   print 'Regular expression is ', reg_ex
   str = raw_input("press enter to continue: ");
   if str=="":
        print "good lets continue"
        infile = codecs.open(inputfile,encoding='utf-8',mode='r')
        outfile = codecs.open(outputfile, encoding='utf-8', mode='w')
        #first_line = infile.readline()
        #index = re.search(r'[^a-zA-Z0-9_]', first_line).start()
        #reg_ex = first_line[index]
        #new_line = re.sub(reg_ex, ' ', first_line)
        #outfile.write(new_line)
        for line in infile:
            line = unidecode(line)
            line = string.lower(line)
            new_line = re.sub(reg_ex, ' ', line)
            outfile.write(new_line)
        infile.close()
        outfile.close()
   else:
        exit(0)

if __name__ == "__main__":
   main(sys.argv[1:])