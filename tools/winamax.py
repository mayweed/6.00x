#!/usr/bin/python

import sys
import math

# Idea: read an input file directly from the command line
# It works but '\n' should be squashed
handp_1 = []
handp_2 = []

with open(sys.argv[1], 'r') as suite:
    n = int(suite.readline()) # first line first number of card
    for i in range(n): handp_1.append(suite.readline())

    n = int(suite.readline()) # n lines second number of card
    for i in range(n): handp_2.append(suite.readline())

print(handp_1, handp_2)

#handp_1 = []
#n = int(input())  # the number of cards for player 1
#for i in range(n):
#        cardp_1 = input()  # the n cards of player 1
#            handp_1.append(cardp_1)
            
#handp_2 = []
#m = int(input())  # the number of cards for player 2
#for i in range(m):
#    cardp_2 = input()  # the m cards of player 2
#    handp_2.append(cardp_2)
                    
# THE FIGHT
#le mieux serait d'écrire une function check_card(card1,card2) qui 
# renvoie la carte la plus élevé ou 0 si les cartes sont
# égales ?
turn = 0
for card in handp_1:
   for cards in handp_2:
   #player one plays an ace
       if card[0] == 'A' and cards[0] != 'A': 
        #peu importe la carte, il gagne
           handp_1.append(cards)
           handp_2.remove(cards)
           turn +=1
                       
       elif card [0] != 'A' and cards[0] == 'A':
           handp_1.remove(card)
           handp_2.append(card)
           turn +=1
                        
       #Player one plays a king
       elif card[0] == 'K' and cards[0] != 'A':
        #peu importe la carte si c'est pas un as, il gagne
           handp_1.append(cards)
           handp_2.remove(cards)
           turn +=1
       elif card [0] == 'K' and cards[0] == 'A':
           handp_1.remove(card)
           handp_2.append(card)
           turn +=1
                            
       # Player 1 plays a Queen
       elif card[0] == 'Q' and (cards[0] != 'A' or cards[0] != 'K'):
           handp_1.append(cards)
           handp_2.remove(cards)
           turn +=1
                            
       # Player one plays a Jack
       elif card[0] == 'J':
           if cards[0] != 'A' or cards[0] != 'K'or cards[0] != 'Q': 
               handp_1.append(cards)
               handp_2.remove(cards)
               turn +=1
                            
       # Reste le cas de 10
       elif card[0] == '1':
           if cards[0] != 'A' or cards[0] != 'K'or cards[0] != 'Q' or cards[0] != 'J':
               handp_1.append(cards)
               handp_2.remove(cards)
               turn +=1
                                    
       # Cas "habituel"
       elif card[0] > cards[0]
               handp_1.append(cards)
               handp_2.remove(cards)
               turn +=1
                            
if not handp_1: print (2, turn) #hand 1 empty, player 2 wins
if not handp_2: print (1, turn) #hand 2 empty, player 1 wins

# WAR

#print (handp_1)
#print (handp_2)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
# print("Debug messages...", file=sys.stderr)
#print("PAT" )
