#!/usr/bin/python

s= input('--> ')
bobcount=0
count=0

while count < (len(s) - 3):
    if s[count:3] == 'bob': 
        bobcount += 1
        count +=2
        print(count)
    else:
        continue
        count +=1

print("Number of bob:" + str(bobcount))
