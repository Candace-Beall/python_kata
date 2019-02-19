import random

winner = ''
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

tie = 'Tie'
computer = 'Computer'

if computer_choice == user_choice:
    winner = tie
elif computer_choice == 'paper' and user_choice == 'rock':
    winner = computer
elif computer_choice == 'rock' and user_choice == 'scissors':
    winner = computer
elif computer_choice == 'scissors' and user_choice == 'paper':
    winner = computer
else:
    winner = 'User'

if winner == tie:
    print('We both chose', computer_choice + ', play again.')
else:
    print(winner, 'won. The computer_chose', computer_choice + '.')
