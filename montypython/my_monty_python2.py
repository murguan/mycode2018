#!/usr/bin/env python3
round = 0           # integer round initiated to 0
while(True):        # sets up an infinite loop condition
    round = round + 1     # increase the round counter
    print('What is the word that start with s _and ends with berry"')
    answer = input()    # string answer collected from user
    if (answer == 'shruberry'): # logic to check if user gave correct answer
        print('You gave the super secret answer!')
        break             # break statement escapes the while loop
    elif (round == 3):    # logic to ensure round has not yet reached 3
        print('Sorry, the answer was shruberry.')
        break             # break statement escapes the while loop
    else:                 # if answer was wrong, and round is not yet equal to 3
        print('Sorry. Try again!')
