#!/usr/bin/python

import math

#!! does not work with float step !!
#Test case 1
start=0
stop=4
step=0.25
r=0

def f(x):
    return 10*math.e**(math.log(0.5)/5.27 * x)

def rectangle_area(start,step):
    '''
        compute the area of a rectangle with length as start point
        and step as width
    '''
    length=f(start)
    return length*step

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
                 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle.
    You can assume that the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to between start and stop times.
    '''
    rad=0.0
    #the amount of radiation
    while start < stop:
        rad+=rectangle_area(start,step) 
        start+=step
 #       print(start,rad)
    return rad
