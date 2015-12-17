#!/usr/bin/python

#from a codingame clash: write a prog that sum the number of a number
# to add the numbers and keep n a str: sum(map(int,str(n))
# if you want a int cast the RIGHT operand

n = int(input("--> "))

def somme(num):
    somme=0
    while num != 0:
        somme += (num%10)
        #in Py3 dont forget the second slash!!
        num //= 10
    return somme


# This code repeats itself need to find sth more terse
summ=somme(n)

#Should be a unique number
while summ >= 10:
    summ += somme(summ)
    summ //=10

print(summ)
