import random

computer = random.randint(1, 6)

you = int(input('Enter your dice roll (1-6): '))

has_guessed = you == computer

print(f'You won: {has_guessed}')