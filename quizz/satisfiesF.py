#!/usr/bin/python

def f(s):
    return 'a' in s

def satisfiesF(L):
    """
    Assumes L is a list of strings

    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
    that f(s) returns True, and no other elements. Remaining elements in L
    should be in the same order.

    Returns the length of L after mutation
    """
    for i in L[:]:
        if f(i)==True:
            continue
        else:L.remove(i)
    return len(L)

#run_satisfiesF(L, satisfiesF)
#L = ['a', 'b', 'a']
L=['aaa', 'bc','h']
print (satisfiesF(L))
print (L)
