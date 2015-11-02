#!/usr/bin/python

s= input('--> ')
bobcount=0
count=0

#while count < (len(s) - 3):
for count in range(len(s)):
    if s[count:count+3] == 'bob': 
        bobcount += 1
        count +=2
    else:
        continue
        count +=1

print("Number of bob:" + str(bobcount))
