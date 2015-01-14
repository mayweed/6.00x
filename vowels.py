#!/usr/bin/python

#s/raw_input()/input()/if py > 3
s = input('--> ')
count=0
for x in s:
    if x == 'a' or x == 'e' or x=='i'\
        or x=='o' or x=='u':
        count +=1
print("Number of vowels: " , str(count))
