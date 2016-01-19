#!/usr/bin/python

#FORMAT: order "salad hamburger water"
#PRINT: [name][:][count][space]
s=input("Give words separated by spaces plz: ")

items=list(s.split())
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

print(count_items)
