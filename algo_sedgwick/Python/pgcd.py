#!/usr/bin/python

"""
This is the first one presented in the book
"""
import sys

#Should cast here
a= int(sys.argv[1])
b= int(sys.argv[2])

def pgcd(p,q):
    if q == 0:
        return p
    r = p%q
    return pgcd(q, r)

x= pgcd(a,b)
print(x)
