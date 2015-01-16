#!/usr/bin/python

s= input('--> ')
count=len(s)
num=0
bobcount=0

for x in s[count]:
    if s[num]=='b' and s[num+1]=='o' and s[num+2]=='b':
        bobcount += 1
        count +=1
    else:
        count +=1
print("Number of bob:" + str(bobcount))
