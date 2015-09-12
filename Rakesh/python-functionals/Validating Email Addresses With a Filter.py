__author__ = 'rakesh'

import re

def filterEmailAddress(email):

    m = re.match(r'\b[a-zA-Z-_0-9]+@[a-zA-Z\d]+[.][a-zA-Z]{1,3}\b', email)

    if m:

        if m.group() == email:
            return email

emailID = []

N = input()

for i in range(N):

    emailID.append(raw_input())

print sorted(list(filter(filterEmailAddress, emailID))) #using filter function in python

