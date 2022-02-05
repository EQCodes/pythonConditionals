# Pin checker with getpass - nitially wasn't working - had to 'Edit Configurations' then 'Emulate terminal in output console'
import getpass
attempts = ['2', '1', '0']


for attempt in attempts:
    pin = getpass.getpass(prompt='Enter your PIN: ')
    if pin != '5678':
        print('Incorrect pin. You have ' + attempt + ' attempts left.')
        continue
    elif pin == '5678':
        print('Thank you, here is 1 million dollars.')
        break


# Working PIN checker without getpass module:
# attempts = ['2', '1', '0']
#
#
# for attempt in attempts:
#     pin = input('Enter your PIN: ')
#     if pin != '5678':
#         print('Incorrect pin. You have ' + attempt + ' attempts left.')
#         continue
#     elif pin == '5678':
#         print('Thank you, here is 1 million dollars.')
#         break
