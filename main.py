# -*- Coding: utf-8 -*-
#
# Author: Art1F4kt
# Description: A simple Guessing Game in Python

from random import randint

def main():
    print('∎∎∎  WELCOME TO THE GUESSING GAME!! ∎∎∎')
    print('\n\n')
    _ = input('PRESS ( ENTER ) TO START')
    chosen_number = randint(0, 100)
    while True:
        guess = input('I\'m thiking in a number between 0-100, type your guess: ')
        if guess.lower() in ('exit', 'quit'):
            print('Right, see you next time!!')
            break
        if not guess.isdigit():
            print('I told you to write number only, not crazy things man!')
            continue
        if int(guess) < chosen_number:
            print('Wrong, The number is GREATER!')
        elif int(guess) > chosen_number:
            print('Wrong, the number is LESSER!')
        else:
            print('C O N G R A T S !!')
            guess = input('Would you like to play again? (Yes/No): ')
            if guess.lower() in ('yes', 'y'):
                continue
            else:
                break

if __name__ == '__main__':
    main()