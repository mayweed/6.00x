#!/usr/bin/python

from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    current_score=0
    # Create a new variable to store the best word seen so far (initially None)  
    best_word=None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(word,hand,wordList):
            # Find out how much making that word is worth
            word_score=getWordScore(word,n)
            # If the score for that word is higher than your best score
            if word_score > current_score:
                current_score=word_score
                best_word=word

    # return the best word you found.
    return best_word


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    score = 0 
    # As long as there are still letters left in the hand:
    #for letters in list(hand.keys()):
    while calculateHandlen(hand) != 0:
        print("Current hand: ",end=''),
        displayHand(hand)
        user_word=compChooseWord(hand,wordList,n)
        if user_word : 
               if isValidWord(user_word,hand,wordList):
                  score+=getWordScore(user_word,n)
                  hand=updateHand(hand,user_word)     
                  print ("\"{0}\" earned {1} points.Total: {2} points.".format(user_word,getWordScore(user_word,n),score))
               else: 
                   print("Invalid word, please try again.")
        else:
            break

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    # I do think we could prevent such a repetition, but "le mieux est l'ennemi du bien"...
    if user_word==None: 
        print("Total Score: ",score)
    else: 
        print("Total Score: ",score)
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    last_hand={}

    #game loop
    while True:
        action=input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ") 
        if action =="n":
            hand=dealHand(HAND_SIZE)
            last_hand=hand
            user_choice=input("Enter u to have yourself play, c to have the computer play: ")
            while user_choice not in ["u","c"]:
                print "invalid command"
                user_choice=raw_input("Enter u to have yourself play, c to have the computer play: ")
                if user_choice in ["u","c"]:break    
            if user_choice=="u":
                playHand(hand,wordList,HAND_SIZE)
            if user_choice=="c":
                compPlayHand(hand, wordList,HAND_SIZE)

        if action=="r":
            if not last_hand:
                print "You have not played a hand yet. Please play a new hand first!"
            else:
                user_choice=input("Enter u to have yourself play, c to have the computer play: ")
                if last_hand and user_choice=="u":
                    playHand(last_hand,wordList,HAND_SIZE)
                if last_hand and user_choice=="c":
                    compPlayHand(last_hand,wordList,HAND_SIZE)

        if action=="e":
            break

        if action not in ["n","r","e"]: print("Invalid Command")

#
# Build data structures used for entire session and play game
#
# cf chapter 6.1.1 in PyTut to explain that
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
