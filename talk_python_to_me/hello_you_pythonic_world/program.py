width = 50
title = 'HELLO APP'
spaces = int((width - len(title)) / 2)

print('-' * width)
print(' ' * spaces + title)
print('-' * width)
print()

name = input('What is your name? ')
greeting = f'Nice to meet you {name}!'

print(greeting)
