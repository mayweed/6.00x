#!/usr/bin/python

import string

#am lazy cant write the 26 letters etc by hand
count=1
print('{',end='')
for i in string.ascii_lowercase: 
    print(i+':'+str(count)+',',end='')
    count+=1
    if count==14: print("\n",end='')
print('}')
