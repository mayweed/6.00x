#!/usr/bin/python

def f(a,b):
    return a+b

def dict_interdiff(d1, d2):
    '''
        d1, d2: dicts whose keys and values are integers
        Returns a tuple of dictionaries according to the instructions above
    '''
#two dict: one for intersect, one for diff. So write to func which returns one dict?
    d3={}
    d4={}

    #intersect
    for key in list(d1.keys()):
        for key2 in list(d2.keys()):
            if key==key2:
                d3[key]=f(d1[key],d2[key])

    #diff
    for key in list(d1.keys()):
        if key not in list(d2.keys()):
            d4[key]=d1[key]
        else: continue

    for key2 in list(d2.keys()): 
        if key2 not in list(d1.keys()):
            d4[key2]=d2[key2]
        else:continue

 #  return (d4)
    return (d3,d4)

d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
d=dict_interdiff(d1,d2)
print(d)
