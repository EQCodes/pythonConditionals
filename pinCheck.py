# Pin checker with getpass - initially wasn't working
# Had to 'Edit Configurations' then 'Emulate terminal in output console'
# NB: correct_pin only seems to work if it is a string
# Sunday updates - made correct_pin a variable, removed continue & switched order of IF statement to simplify

import getpass
attempts = ['2', '1', '0']
correct_pin = '5678'

for attempt in attempts:
    pin = getpass.getpass(prompt='Enter your PIN: ')
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