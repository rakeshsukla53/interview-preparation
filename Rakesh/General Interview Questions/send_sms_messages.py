__author__ = 'rakesh'

import requests

message = raw_input('Enter the message')
number = raw_input('Enter your number')


payload = {'number': number, 'message': message}
r = requests.post("http://textbelt.com/text", data=payload)
if r.json()['success']:
    print('Success!')
else:
    print('Error!')

