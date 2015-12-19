#!/usr/bin/python

"""
Given a certain number you should print a pyramid of that number:
Input: 3
Output:
333
33
3
INTERESTING: learning print() formatting
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
