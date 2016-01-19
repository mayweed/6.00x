#!/usr/bin/python
# this is a rewrite exercise of count() method
# do NOT use count is a goal in itself!!

# TODO: the corner case where i is NOT prev
# BUT is already a value, should just update the key
# s= salad hamburger water hamburger

s=input("Give words separated by spaces plz: ")

items=list(s.split())
count_items={}

count=0
y=0

#pour chaque prev il faut parcourir toute la liste
while y < len(items)-1:
    prev=items[y]
    for i in items[y:]:
        print(i)
        if i==prev:
            #should we del() here?or slice??
            count +=1
            count_items[i]=count
        elif i != prev: #or items.index(i) == len(items)-1:
            continue
        #when one i is unique? and (after..) not in items?
        else:count=1;count_items[i]=count
    y+=1


print(count_items)
