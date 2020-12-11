#! /usr/bin/env python 
# 会去环境设置寻找 python 目录
# -*- coding: UTF-8 -*-
######## stage define

import sys, getopt

def parse(inputfile,outputfile):
    S_START = 0;
    S_CODEC = 1;
    S_DONE = 2;
    
    stage = S_START;
    
    with open(inputfile, 'r') as fp:
    line = fp.readline()               # 调用文件的 readline()方法   
    while line:
        print("###:",line);
        if stage == S_START:
            if line.find("---"):
                stage = S_CODEC;
                print("aa",line);
        elif stage == S_CODEC:
            stage = S_DONE;
            for i in range(1,7):
                print("bb",line);
                line = fp.readline()
        
        line = fp.readline()
        
                

def main(argv):
   inputfile = ''
   outputfile = "output.csv"
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print ('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
         
   
#   print ('input file:', inputfile)
#   print ('output file:', outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])                