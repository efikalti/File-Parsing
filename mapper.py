#!/usr/bin/env python
import sys
import re, string
from operator import itemgetter

reg_ex = '|'

#open files
file2 = open(sys.argv[1], "r")
#read fields of file1
fields1 = sys.stdin.readline().strip().split(reg_ex)
#read fields of file 2
fields2 = file2.readline().strip().split(reg_ex)
#read every line of file2 into one variable
file2_lines = file2.readlines()
#parse every line of file1
num1 = 2
for line in sys.stdin:
  line = line.strip()
  #split the lines into parts
  parts1 = line.split(reg_ex)
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
    num2 = num2 + 1
  num1 = num1 + 1
file2.close()