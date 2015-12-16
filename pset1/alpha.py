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

end=0
start=0

for i in range(len(s)-1):
    if s[i] > s[i+1]:
        #end +=1
        continue
    if s[i] == s[i+1]:
        #end +=1
        continue
    if s[i] < s[i+1]:
        print(s[start:i])
        print(start,i,file=sys.stderr)
        #la fin devt le nouveau début
        start = i

