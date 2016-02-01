#!/usr/bin/python

# 6.00 Problem Set 3
# 
# Hangman game
#
import random
import string

WORDLIST_FILENAME='/home/guillaume/scripts/6.00x/pset3/hangman/words.txt'

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")

    # inFile: file
    with open(WORDLIST_FILENAME,'r',1) as inFile:
        line = inFile.readline()

    # wordlist: list of strings
    wordlist = line.split()
    print ("{0} words loaded.".format(len(wordlist))) 
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count=len(secretWord)
    
    for i in secretWord:
        if i in lettersGuessed: count-=1
        else: continue
                                           
    if count ==0: return True
    else: return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    secretword_bis=''
    for i in secretWord:
        if i in lettersGuessed: secretword_bis+=i
        else: secretword_bis+=' _ '
    return secretword_bis

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters=string.ascii_lowercase 
    letters_bis=''
    for i in letters:
        if i in lettersGuessed:continue
        else:letters_bis+=i
    return letters_bis

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    print("Welcome to the game Hangman!")
    print("I'm thinking about a word that is {0} letters long".format(len(secretWord)))
    print("-----------")

    #you always got 8 guesses. Why? Because...
    guesses= 8
    letters_guessed=[]
    word=''

    count_guess=guesses
    count=0
    #game loop
    while count <= guesses:
        print("You have {0} guesses left".format(count_guess))
        print("Available Letters: {0}".format(getAvailableLetters(letters_guessed)))
        user_guess=input("Please guess a letter: ")

        if user_guess in string.ascii_uppercase: 
            user_guess=user_guess.lower()

        if user_guess in letters_guessed: 
            print("Oops! You've already guessed that letter: {0}".format(getGuessedWord(secretWord,letters_guessed)))
            print("-----------")
            continue
        if user_guess in secretWord:
            letters_guessed.append(user_guess)
            print("Good guess: {0}".format(getGuessedWord(secretWord,letters_guessed)))
        if user_guess not in secretWord:
            print("Oops! That letter is not in my word: {0}".format(getGuessedWord(secretWord,letters_guessed)))
            count_guess -=1
            count +=1 

        if isWordGuessed(secretWord,letters_guessed): 
            print("-----------")
            print("Congratulations! You Won!")
            break
        if count_guess==0 and getGuessedWord(secretWord,letters_guessed) != secretWord:
            print("-----------")
            print("Sorry you ran out of guesses! The word was else")
            break

        print("-----------")
        letters_guessed.append(user_guess)

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
