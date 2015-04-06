#!/usr/bin/env python  
import sys  
from operator import itemgetter
      
# input comes from STDIN,the mapper provides for it  
#for every line we get from stdin  
for line in sys.stdin:
	line = line.strip()
	print line