#!/usr/bin/python

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

for i in range(len(s)-1):
    start=0
    end=0
    if s[i] > s[i+1]:
        end +=1
    #    continue
    if s[i] == s[i+1]:
        end +=1
     #   continue
    if s[i] < s[i+1]:
        print(s[start:end])
        chunks.append(s[start:end])
        start = i+1
      #  break

print(chunks)
