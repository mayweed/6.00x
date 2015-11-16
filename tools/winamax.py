#!/usr/bin/python

import sys
import math

# Idea: read an input file directly from the command line
# It works but '\n' should be squashed
handp_1 = []
handp_2 = []

with open(sys.argv[1], 'r') as suite:
    n = int(suite.readline()) # first line first number of cardp_1
    for i in range(n): handp_1.append(suite.readline())

    n = int(suite.readline()) # n lines second number of cardp_1
    for i in range(n): handp_2.append(suite.readline())

print(handp_1, handp_2)

#handp_1 = []
#n = int(input())  # the number of cardp_2 for player 1
#for i in range(n):
#        cardp_1p_1 = input()  # the n cardp_2 of player 1
#            handp_1.append(cardp_1p_1)
            
#handp_2 = []
#m = int(input())  # the number of cardp_2 for player 2
#for i in range(m):
#    cardp_1p_2 = input()  # the m cardp_2 of player 2
#    handp_2.append(cardp_1p_2)
                    
# THE FIGHT
#le mieux serait d'écrire une function check_cardp_1(cardp_11,cardp_12) qui 
# renvoie la carte la plus élevé ou 0 si les cartes sont
# égales ?
def check_cardp_1(cardp_1,cardp_2):
    """ check card, returns the best one"""
    if cardp_1[0] == 'A' and cardp_2[0] != 'A': 
        return cardp_1
                       
    elif cardp_1[0] != 'A' and cardp_2[0] == 'A':
        return cardp_2
                        
    #Player one plays a king
    elif cardp_1[0] == 'K' and cardp_2[0] != 'A':
        return cardp_1

    elif cardp_1 [0] == 'K' and cardp_2[0] == 'A':
        return cardp_2
                            
    # Player 1 plays a Queen
    elif cardp_1[0] == 'Q' and (cardp_2[0] != 'A' or cardp_2[0] != 'K'):
        return cardp_1
                            
    # Player one plays a Jack
    elif cardp_1[0] == 'J':
        if cardp_2[0] != 'A' or cardp_2[0] != 'K'or cardp_2[0] != 'Q': 
            return cardp_1
                            
    # Reste le cas de 10
    elif cardp_1[0] == '1':
        if cardp_2[0] != 'A' or cardp_2[0] != 'K'or cardp_2[0] != 'Q' or cardp_2[0] != 'J':
            return cardp_1
                                    
    # Cas "habituel" 
    if cardp_1[0] and cardp_2[0] not in ['A','K', 'Q','J','1']: 
        if cardp_1[0] > cardp_2[0]
            return cardp_1
        else: #cardp_1[0] < cardp_2[0]:
            return cardp_2 


# GAME IMPLEMENTATION
turn = 0                
for cardp_1 in handp_1:
    for cardp_2 in handp_2:
        #en definitive y'a que 2 cas: soit l'un gagne soit l'autre
        # list comprehensions: remove() method results in x not in list!!
        handp_1 = [card for card in cardp_2 if check_card(cardp_1, cardp_2) == cardp_1]
        handp_2 = [cards for cards in cardp_1 if check_card(cardp_1, cardp_2) == cardp_2]
        #if check_card(cardp_1,cardp_2)==cardp_1:
        #   handp_1.append(cardp_2)
        #handp_2.remove(cardp_2)
        #else:
        #   handp_2.append(cardp_1)
        #handp_1.remove(cardp_1)
    turn +=1

if not handp_1: print (2, turn) #hand 1 empty, player 2 wins
if not handp_2: print (1, turn) #hand 2 empty, player 1 wins

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
# print("Debug messages...", file=sys.stderr)
#print("PAT" )
