# Pin checker with getpass - initially wasn't working
# Had to 'Edit Configurations' then 'Emulate terminal in output console'
# NB: correct_pin only works as a string unless I put int() before getpass.getpass, but len() wouldn't work unless str
# Sun. updates: correct_pin variable, simplified IF statement, removed continue, limited pin to 4, removed 'prompt'

import getpass
attempts = ['2', '1', '0']
correct_pin = '5678'

for attempt in attempts:
    pin = getpass.getpass('Enter your PIN: ')
    if len(pin) > 4:
        print("Your PIN was too long - please enter 4 characters.")
        continue
    if pin == correct_pin:
        print('Thank you, here is 1 million dollars.')
        break
    else:
        print('Incorrect pin. You have ' + attempt + ' attempts left.')

# Working PIN checker without getpass module, with continue still in if statement and pin not a variable:
# attempts = ['2', '1', '0']
#
# for attempt in attempts:
#     pin = input('Enter your PIN: ')
#     if pin != '5678':
#         print('Incorrect pin. You have ' + attempt + ' attempts left.')
#         continue
#     elif pin == '5678':
#         print('Thank you, here is 1 million dollars.')
#         break
