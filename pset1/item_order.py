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
prev=items[0]

for i in items:
    print(i)
    if i==prev:
        count +=1
        count_items[i]=count
    if i != prev or items.index(i) == len(items)-1:
        count_items[prev]=count
        prev=i
        count=1

print(count_items)
