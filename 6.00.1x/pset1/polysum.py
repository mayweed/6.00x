#!/usr/bin/python

import math

def polysum(n,s):
    """
        This function takes as input the number of sides n and the length
        of each side s of a polygon. It returns as output the sum of the
        area and the square of the polygon perimeter .
    """
    def perimeter(numberofside,length):
        return numberofside*length

    def area(numberofside,length):
        aire=((0.25*n*s**2)/math.tan(math.pi/n))
        return round(aire,2)

    return round(area(n,s)+perimeter(n,s)**2,4)
