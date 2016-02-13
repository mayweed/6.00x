#!/usr/bin/python

def flatten(aList):
    ''' 
    >>> l=[[1, 2, 3], 'a']
    >>> l=l[0]+l[1]
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: can only concatenate list (not "str") to list
    >>> l=l[0]+[l[1]]
    >>> l
    [1, 2, 3, 'a']
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    liste=[]

    #base case: if there is no list in aList, just return aList

    #else if there is a list, try to flatten it thanks to the recursive use of flatten()
    #on a copy of a list..so: if an elt is _not_ a list, append to liste[] else flatten via +
    #then repeate on aList - elt...

test_mit=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
first_test=[[1,2,3],'a']
flatten(test_mit)
