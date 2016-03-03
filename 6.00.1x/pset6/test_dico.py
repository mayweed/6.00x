#!/usr/bin/python

import string

# does NOT work in circle(cf x/y/z)

def build_shift_dict(shift):
    '''
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to a
    character shifted down the alphabet by the input shift. The dictionary
    should have 52 keys of all the uppercase letters and all the lowercase
    letters only.        
        
    shift (integer): the amount by which to shift every letter of the 
    alphabet. 0 <= shift < 26

    Returns: a dictionary mapping a letter (string) to 
             another letter (string). 
    '''
    #cant use mk_dict in the IDE
    #one or two dicos??
    # no: use ord + shift mod 26?? cf wikipedia
    minuscules=string.ascii_lowercase
    maj=string.ascii_uppercase
    dico={}

    for i in range(len(minuscules)):
    #c'est l'indice qui change ne pas oublier les () pour la précédence
        dico[minuscules[i]]= minuscules[(i+shift)%26] 
        
    for i in range(len(maj)):
    #c'est l'indice qui change ne pas oublier les () pour la précédence
        dico[maj[i]]= maj[(i+shift)%26] 

    print(dico)


build_shift_dict(0)
