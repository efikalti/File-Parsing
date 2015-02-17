import sys, getopt
from unidecode import unidecode
import codecs
import re, string

def main(argv):
   inputfile = ''
   outputfile = ''
   reg_ex = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:r:",["ifile=","ofile=","regex="])
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
   str = raw_input("enter c to continue: ")
   if str=="c":
        print "good lets continue."
        infile = codecs.open(inputfile,encoding='utf-8',mode='r')
        outfile = codecs.open(outputfile, encoding='utf-8', mode='w')
        for line in infile:
            s = '[^' + reg_ex + '\w -]+'
            line = re.sub(s, '', line)
            reg_sub = '[' + reg_ex + ']+'
            line = re.sub(reg_sub, reg_ex, line)
            line = unidecode(line)
            line = string.lower(line)
            fields = line.split(reg_ex)
            final_string = '|'
            for field in fields:
              field = re.sub(r'[^\w.-]+', ' ', field)
              field = string.strip(field)
              final_string = final_string + field + '|'
            #outfile.write(final_string)
            print final_string
        infile.close()
        outfile.close()
   else:
        exit(0)

if __name__ == "__main__":
   main(sys.argv[1:])