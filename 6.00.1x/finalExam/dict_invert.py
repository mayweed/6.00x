#!/usr/bin/python

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    dico_inv={}
    for k,v in d.items():
        if v in list(dico_inv.keys()):
            dico_inv[v].append(k)
            dico_inv[v].sort()
        else:
            dico_inv[v]=[k]
    return dico_inv

#d={1:10, 2:20, 3:30}
#d = {1:10, 2:20, 3:30, 4:30}
#d = {4:True, 2:True, 0:True}
d={0: 9, 9: 9, 5: 9}
print(dict_invert(d))
