print('i like your butt')

bank_balance = 900
ferrari_cost = 8500

print(f'{bank_balance} {ferrari_cost}')
print(str(bank_balance) + ' ' + str(ferrari_cost))

if bank_balance >= ferrari_cost:
    print('Why not?')
    print('Go ahead, buy it')
else:
    print('Sorry')
    print('Try again next week')

print('-' * 20)

number_of_scoops = -1
if number_of_scoops == 0:
    print('You didn''t want any ice cream?')
    print('We have lots of flavors.')
elif number_of_scoops == 1:
    print('A single scoop for you, coming up.')
elif number_of_scoops == 2:
    print('Oh, two scoops for you!')
elif number_of_scoops >= 3:
    print('Wow, that''s a lot of scoops!')
else:
    print('I''m sorry, I can''t give you negative scoops.')

print('-' * 20)

#
# import random
# random_choice = random.randint(0,2)
# if random_choice == 0:
#     computer_choice = 'rock'
# elif random_choice == 1:
#     computer_choice = 'paper'
# else:
#     computer_choice = 'scissors'
# print('The computer chooses', computer_choice)
#
#
# import random
# random_choice = random.randint(0,2)
# if random_choice == 0 :
#     computer_choice = 'rock'
# elif random_choice == 1:
#     computer_choice = 'paper'
# else:
#     computer_choice = 'scissors'
#
#
# while True:
#     user_choice = input('rock, paper or scissors? ')
#     if user_choice in ['rock', 'paper', 'scissors']:
#         break
#     print(f'{user_choice} is invalid...')
#
# print('You chose' , user_choice, 'and the computer chose', computer_choice )


print('-' * 20)
print('-' * 20)

import random

winner = 'your butt'
random_choice = random.randint(0, 2)
if random_choice == 0:
    computer_choice = 'rock'
elif random_choice == 1:
    computer_choice = 'paper'
else:
    computer_choice = 'scissors'

while True:
    user_choice = input('rock, paper or scissors? ')
    if user_choice in ['rock', 'paper', 'scissors']:
        break
    print(f'{user_choice} is invalid...')

print('You chose', user_choice, 'and the computer chose', computer_choice)

if computer_choice == user_choice:
    winner = 'Tie'
elif computer_choice == 'rock' and user_choice == 'scissors':
    winner = 'computer'
elif computer_choice == 'paper' and user_choice == 'rock':
    winner = 'computer'
elif computer_choice == 'scissors' and user_choice == 'paper':
    winner = 'computer'
else:
    winner = 'user'

print(f'The winner is {winner}')
