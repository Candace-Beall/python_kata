import random

from talk_python_to_me.helpers.header import print_header

print_header('GUESS THAT NUMBER GAME', 65)

the_number = random.randint(0, 100)

guess_text = input('Guess a number between 0 and 100: ')
guess = int(guess_text)

if the_number > guess:
    print('too low')
elif the_number < guess:
    print('too high')
else:
    print('you win')
