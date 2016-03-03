#!/usr/bin/python

# git remote add origin https://github.com/mayweed/6.00x.git
# git push -u origin master

#s/raw_input()/input()/if py > 3
s = input('--> ')
count=0
for x in s:
    if x in ['a','e','i','o','u']:
        count +=1
print("Number of vowels: " , count)
