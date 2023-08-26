from functions import *


user_choice = input('type (e)ncode or (d)ecode Morse code: ')

if user_choice.lower() == 'e':
    user_text = input('Enter your string: ')
    result = encode(user_text)
    print(f'Your Encoded Morse Code is: {result}')
elif user_choice.lower() == 'd':
    user_text = input('Enter your string: ')
    result = decode(user_text)
    print(f'Your Decoded Morse Code is: {result}')
else:
    print('Invalid option')
    exit(1)
