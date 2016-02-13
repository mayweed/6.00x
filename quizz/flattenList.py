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
    count=0
    while count < len(aList):
        if type(aList[count])==list and type(aList[count+1]) != list:
            liste=aList[count]+[aList[count+1]]
        count+=1
    print(liste)

flatten([[1,2,3],'a'])
