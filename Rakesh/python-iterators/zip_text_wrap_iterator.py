__author__ = 'rakesh'

s = '1234567890'
print list(map(''.join, zip(*[iter(s)]*2)))


