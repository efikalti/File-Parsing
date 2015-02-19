#!/usr/bin/env python
import sys, codecs

reg_ex = '|'

def main(argv):
   #argument variables
   inputfile = ''
   outputfile = ''
   reg_ex = ''
   # try-loop to assign the given arguments to the variables
   try:
      opts, args = getopt.getopt(argv,"ho:",["file1=","file2=","ofile="])
   except getopt.GetoptError:
      print 'usage: test.py --file1=<first_file> --file2=<second_file> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("--file1"):
         filename1 = arg
      elif opt in ("--file2"):
         filename2 = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print 'First file is', filename1
   print 'Second file is', filename2
   print 'Output file is ', outputfile
   #get confirmation that the given arguments are right to continue
   str = raw_input("enter c to continue: ")
   if str=="c":
        #open files
        file1 = codecs.open("filename1", encoding="utf-8", mode="r")
        file2 = codecs.open("filename2", encoding="utf-8", mode="r")
        outfile = codecs.open("outputfile", encoding="utf-8", mode="w")
        #read fields of file1
        fields1 = file1.readline().split(reg_ex)
        #read fields of file 2
        fields2 = file2.readline()split(reg_ex)
        #close files
        file1.close()
        file2.close()
        outfile.close()
   else:
        exit(0)

if __name__ == "__main__":
   #call main with the arguments, exluding the first one (it is the name of the script)
   main(sys.argv[1:])