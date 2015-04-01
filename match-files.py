#!/usr/bin/env python
import sys, getopt
from unidecode import unidecode
import codecs
import re, string

reg_ex = '|'

def main(argv):
   #argument variables
   outputfile = ''
   filename1 = ''
   filename2 = ''
   # try-loop to assign the given arguments to the variables
   try:
      opts, args = getopt.getopt(argv,"ho:",["file1=","file2=","output="])
   except getopt.GetoptError:
      print 'usage: match-files.py --file1=<first_file> --file2=<second_file> --ofile=<outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("--file1"):
         filename1 = arg
      elif opt in ("--file2"):
         filename2 = arg
      elif opt in ("-o", "--output"):
         outputfile = arg
   print 'First file is', filename1
   print 'Second file is', filename2
   print 'Output file is ', outputfile
   #get confirmation that the given arguments are right to continue
   answer = raw_input("enter c to continue: ")

   if answer=="c":
        #open files
        file1 = open(filename1,"r")
        file2 = open(filename2, "r")
        #outfile = open(outputfile, "w")
        
        #read fields of file1
        fields1 = file1.readline().strip().split(reg_ex)
        #read fields of file 2
        fields2 = file2.readline().strip().split(reg_ex)
        #read every line of file2 into one variable
        file2_lines = file2.readlines()
        #parse every line of file1
        num1 = 2
        for line in file1:
            #split the lines into parts
            parts1 = line.strip().split(reg_ex)
            #parse every line of file2
            num2 = 2
            for line2 in file2_lines:
              output = ''
              parts2 = line2.strip().split(reg_ex)
              for part1 in parts1:
                for part2 in parts2:
                  words = part2.strip().split(' ')
                  for word in words:
                    if word in part1.split(' '):
                      output = output + word + ' '
              output = re.sub(r'\W[^A-Za-z0-9|]\W', "", output)
              if output != '':
                output = output + ' | line_in_file_1: ' + str(num1) + ' | line_in_file_2: ' + str(num2) + '\n'
                print output
                #outfile.write(output)
              num2 = num2 + 1
            num1 = num1 + 1
        #close files
        file1.close()
        file2.close()
        #outfile.close()
   else:
        exit(0)

if __name__ == "__main__":
   #call main with the arguments, exluding the first one (it is the name of the script)
   main(sys.argv[1:])