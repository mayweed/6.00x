#!/usr/bin/python

# Must use bisection search
# Do not forget: update high/low separately. Middle is a formula!!
low=0
high=100
guessed=False

print("Please think of a number between 0 and 100!")

#I do like the use of this boolean
while not guessed:
    #middle is a formula
    guess=(high+low)/2
    print("Is your secret number {0} ?".format(guess))
    user_hint=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low."
    "Enter 'c' to indicate I guessed correctly.")
    if user_hint=='h':
        #if it's too high, it's good new high ;)
        high=guess
    elif user_hint=='l':
        low=guess
    elif user_hint=='c':
        guessed=True
    else:
        print("Sorry, I did not understand your input.")

print('Game over. Your secret number was: {0}'.format(guess))
    
