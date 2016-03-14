#!/usr/bin/python

def getSublists(L, n):
    """
    This function returns a list of all possible sublists in L of length n without skipping elements in L.
    The sublists in the returned list should be ordered in the way they appear in L, with those sublists 
    starting from a smaller index being at the front of the list.
    """
    ListeOfSub=[]
    #ListeOfSub.append([x for x in L for y in range(n)])
    #use index + range with its 3 args!!
    x=0
    while x < len(L):
        ListeOfSub.append([L[i:i+n] for i in range(x,len(L),n)]) 
        x+=1
    print(ListeOfSub)
            
getSublists([1,2,3,4],2)
