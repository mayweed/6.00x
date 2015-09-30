#!/usr/bin/python

s= input('--> ')
bobcount=0
count=0

for y in s[len(s)-1]:
    if y==b and y+1==o and y+2==b:
        bobcount += 1

print("Number of bob:" + str(bobcount))
