# -*- Coding: utf-8 -*-
#
# Author: Art1F4kt
# Description: A simple Guessing Game in Python

from random import SystemRandom

def main():
    tips = 0
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
            # Adding some type of randomness in the prhases to make the game less bored
            print(
                random.choice([
                    'Type a valid number...Please', 
                    'Be more careful, when typing numbers so that letters don\'t come together',
                    'I asked a number, not a crazy message!'
                ])
            )
            continue
        
        if int(guess) < chosen_number:
            print(random.choice([
                'Nop, the number is Higher!!',
                'It is close! The number is Greater',
                'Almost, the number is Greater than that'
            ]))
        elif int(guess) > chosen_number:
            print(random.choice([
                'Nah, the number is Lower!! Haha!',
                'It passed by barely! The number is Lesser',
                'Almost, the number is Lesser than that'
            ]))
        else:
            congrats = random.choice(['CONGRATS', 'WELL DONE', 'AMAZING'])
            print(f'{congrats}!! You Guessed it in {attemps} Attemps!!')
            guess = input('Would you like to play again? (Yes/No): ')
            if guess.lower() in ('yes', 'y'):
                attemps = 0
                chosen_number = random.randint(0, 100)
                print('Try to guess the number I\'m thinking, between 0-100')
                continue
            else:
                break
        
        if attemps >= 10 and tips == 0:
            guess = input('Would like a better tip? (Yes/No): ').lower()
            if guess in ('yes', 'y'):
                hint = 'Even' if chosen_number % 2 == 0 else 'Odd'
                print(f'The number that i\'m thinking is {hint}')
            tips += 1

        attemps += 1

if __name__ == '__main__':
    main()