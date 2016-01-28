#!/usr/bin/python

def ndigits(number):
    """
        This function takes as input a number postive or negative and outputs the number of
        digits in number.
    """
    count=1
    if abs(number//10) == 0:return 1
    else:return count+1*ndigits(abs(number//10))
