#!/usr/bin/python

s= input('--> ')
count=0
bobcount=0

for x in s:
    if s[count]=='b' and s[count+1]=='o' and s[count+2]=='b':
        bobcount += 1
        count +=1
    else
        count +=1
