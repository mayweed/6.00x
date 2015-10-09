#!/usr/bin/python

s= input('--> ')
bobcount=0
count=0

for y in s[len(s)-1]:
      if s[count]=='b':
         if s[count+1] =='o':
            if s[count+2]=='b':
               bobcount += 1
      count +=3

print("Number of bob:" + str(bobcount))
