#!/usr/bin/python

def item_order(order):
    """
    This must be written as a function which must return sth
    here a well-formatted string
    """
    items=list(order.split())
    count_items={'salad':0,'hamburger':0,'water':0}
    count=0
    y=0
    while y <= len(items)-1:
        prev=items[y]
        for i in items:
            if i==prev:
                count +=1
                count_items[i]=count
        count=0
        y+=1
    #string formatting cf 7.1.1 Python Tut
    result='salad:{salad:d} hamburger:{hamburger:d} water:{water:d}'.format(**count_items)
    return result
