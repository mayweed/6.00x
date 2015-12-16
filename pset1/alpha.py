#!/usr/bin/python

import sys

s= input("--> ")
"""
ALGO
Translate string s in a list of ord(s) int
Check if s > s+1
If not, append the preceding chunk to the list
Retranslate it to a string?
"""
#a new list where append the new chunks
chunks=[]

#String manip:
#http://www.pythonforbeginners.com/basics/string-manipulation-in-python
#http://pythoncentral.io/cutting-and-slicing-strings-in-python/
#end is i
for i in range(len(s)-1):
    start=0
    if s[i] < s[i+1]:
        continue
    if s[i] == s[i+1]:
        continue
    #need to handle end of line...
    if s[i] > s[i+1] or i+1 == len(s)-1:
        print(s[start:i+1])
        print(start, i+1, file=sys.stderr)
        #la fin devt le nouveau début
        start = i+1
