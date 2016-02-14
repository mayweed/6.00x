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
    for i in aList:
        if type(i)==list:
            #if list in i flatten!!
            liste+=flatten(i)
        else:liste.append(i)
    print(liste)
    #if len(aList) <=1: return aList
    #if list then check for list, stop condition: not list(append)
    #should slice the list
    #tant que y'a des objets liste il faut flatten..

    #else if there is a list, try to flatten it thanks to the recursive use of flatten()
    #on a copy of a list..so: if an elt is _not_ a list, append to liste[] else flatten via +
    #then repeate on aList - elt...

test_mit=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
first_test=[[1,2,3],'a']
test_bc=[1,2,3,['a','b']]
flatten(test_mit)
