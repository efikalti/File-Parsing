import sys, getopt
from unidecode import unidecode
import codecs
import re, string

def main(argv):
   #argument variables
   inputfile = ''
   outputfile = ''
   reg_ex = ''
   # try-loop to assign the given arguments to the variables
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
   #get confirmation that the given arguments are right to continue
   str = raw_input("enter c to continue: ")
   if str=="c":
        print "good lets continue."
        #open the files for input and output
        infile = codecs.open(inputfile,encoding='utf-8',mode='r')
        outfile = codecs.open(outputfile, encoding='utf-8', mode='w')
        #parse every line of the input file
        for line in infile:
            #replace all non-latin characters with latin ones
            line = unidecode(line)
            #make the every character lowercase
            line = string.lower(line)
            #remove every regular expression excluding the one from the arguments and some others
            #like '-'
            s = 'r[^' + reg_ex + '\w -]+'
            line = re.sub(s, '', line)
            #remove multiple appearances of the argument reg_ex
            reg_sub = '[' + reg_ex + ']+'
            line = re.sub(reg_sub, reg_ex, line)
            #split the line in pieces, each separated by the reg_ex
            fields = line.split(reg_ex)
            #use a new reg_ex to separate the fields
            final_string = '|'
            for field in fields:
              #field = re.sub(r'[^\w.-]+', ' ', field)
              #strip line from trailing whitespaces
              field = string.strip(field)
              #join the finally clean field to a final string
              final_string = final_string + field + '|'
            #write the final string, containing the fields separates by | to the output file
            #outfile.write(final_string)
            print final_string
        #close the files
        infile.close()
        outfile.close()
   else:
        exit(0)

if __name__ == "__main__":
   #call main with the arguments, exluding the first one (it is the name of the script)
   main(sys.argv[1:])