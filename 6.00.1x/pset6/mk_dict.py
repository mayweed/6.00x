#!/usr/bin/python

import string

#am lazy cant write the 26 letters etc by hand
#could reuse that: in a func + python -c?? Argv??
#The last comma is not a problem...ouf...
def mk_dict(L):
    '''
        Take an iterable
        Return a dict numbered from 0
    '''
    count=0
    print('{',end='')
    for i in L:
        print("\'{0}\':{1},".format(i,str(count)),end='')
        count+=1
        if count==14: print("\n",end='')
    print('}')

### TESTING ###
mk_dict(string.ascii_uppercase)
#mk_dict(['a','b','c'])
