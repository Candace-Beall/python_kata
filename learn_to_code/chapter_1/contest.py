import random

print(__name__)
customers = ['Aubrey', 'Kaiden', 'Jordan', 'Epik']

winner = random.choice(customers)

flavor = 'vanilla'

print('Congratulations ' + winner + ' you have won an ice cream sumdae!')

prompt = 'Would you like a cherry on top? '

wants_cherry = input(prompt)

order = flavor + ' sundae'

if wants_cherry == 'yes':
    order += ' with a cherry on top'

print('One ' + order + ' for ' + winner + ' coming right up...')
