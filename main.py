# -*- Coding: utf-8 -*-
#
# Author: Art1F4kt
# Description: A simple Guessing Game in Python

from random import SystemRandom

def main():
    attemps = 0
    random = SystemRandom()
    chosen_number = random.randint(0, 100)
    print('∎∎∎  WELCOME TO THE GUESSING GAME!! ∎∎∎')
    print('\n')
    print('Try to guess the number I\'m thinking, between 0-100')
    while True:
        guess = input('Type your guess: ')
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
            print(f'CONGRATS !! You Guessed it in {attemps} Attemps!!')
            guess = input('Would you like to play again? (Yes/No): ')
            if guess.lower() in ('yes', 'y'):
                continue
            else:
                break

        attemps += 1

if __name__ == '__main__':
    main()