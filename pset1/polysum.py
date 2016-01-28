#!/usr/bin/python

import math

def polysum(n,s):
    def perimeter(numberofside,length):
        return numberofside*length

    def area(numberofside,length):
        aire=((0.25*n*s**2)/math.tan(math.pi/n))
        return round(aire,2)
    return round(area(n,s)+perimeter(n,s)**2,4)
