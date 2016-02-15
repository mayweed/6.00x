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

    #base case
    if len(aList) ==0: 
        return aList

    for element in aList:
        if type(element)==list:
            for item in (element):
                if type(item)==list:
                    liste+=flatten(item)
                else:liste.append(item)
        else:liste.append(element)

    return liste 

test_mit=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
first_test=[[1,2,3],'a']
test_bc=[1,2,3,['a','b']]

i=flatten(test_mit)
print(i)
