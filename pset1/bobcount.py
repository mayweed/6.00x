#!/usr/bin/python

s= input('--> ')
bobcount=0
count=0

for y in s[len(s)-1]:
#use s[y] !!
    while count < (len(s) -1):
        if s[count]=='b':
            if s[count+1] =='o':
                if s[count+2]=='b':
                    bobcount += 1
    count +=1

print("Number of bob:" + str(bobcount))
