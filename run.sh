#! /bin/bash
#"hdfs://localhost:9000/user/efi/test.txt",
#-file 'home/efi/Projects/File-Parsing/test.txt' \

hadoop jar $HADOOP_PREFIX/hadoop-streaming.jar \
-file '/home/efi/Projects/File-Parsing/wordcount-mapper.py' \
-mapper '/home/efi/Projects/File-Parsing/wordcount-mapper.py french.txt' \
-file '/home/efi/Projects/File-Parsing/reducer.py'  \
-reducer '/home/efi/Projects/File-Parsing/reducer.py' \
-file '/home/efi/Projects/File-Parsing/french.txt'  \
-input /user/efi/input -output /user/efi/output