#! /usr/bin/env python 
# 会去环境设置寻找 python 目录
# -*- coding: UTF-8 -*-

# . data type
# 1. if/else
# . argc/argv
import sys
import re

print ("Hello, Python!")

############################## 1. data type

counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "Johnson" # 字符串

## 1. str operation
str0 = name[1:5]                                # 选择1~5个字符,不包括第5个字符
str1 = name[1:-1]                               # 从第一个到倒数一个，不包括倒数一个
#print(str0)
#print(str1)

## 2. list 
list1 = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'mike']
sublist = list1[1:3]                             # 第二个至第三个元素
addlist = list1 + tinylist
#print(sublist)
#print(addlist)
############################## 1. 1f/else
val = 10

if  val < 5: 
   print(val , "<5")
elif  val < 15:  
   print(val , "<15")
else :  
   print(val , ">=15")
   
def usage(exitval):
    print(
    """
    Usage: 
    """
    )
    
    sys.exit(exitval)

#
if __name__ == "__main__":
    argc = len(sys.argv)
    arg1 =""
    arg2 =""
    if (argc > 1): arg1 = sys.argv[1]
    if (argc > 2): arg2 = sys.argv[2]
    
    if(argc > 3):
        usage(1)
        
#    print("argc =",argc);
#    print("para1 =",arg1);
#    print("para2 =",arg2);
        
    exit(1)
    