#!/usr/bin/python

"""
Given a certain number you should print a pyramid of that number:
Input: 3
Output:
333
33
3
INTERESTING: learning print() formatting
https://docs.python.org/3/library/functions.html#print
"""
n=int(input("--> "))
i=0
z=n

while i <= n:
    for y in range(z):
    # no newline, new end
        print(n,end="")
    z -=1
    i += 1
    print(end="\n")
