#!/usr/bin/python

def dotProduct(listA, listB):
    '''
        listA: a list of numbers
        listB: a list of numbers of the same length as listA
    '''
    product=0
    #lists got same length...(way easier...)
    length=len(listA)
    while length !=0:
            product+=(listA.pop()*listB.pop())
            length -=1
    #use return here to validate
    print(product)

dotProduct([1, 2, 3],[4,5,6])
