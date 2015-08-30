__author__ = 'rakesh'

import hashlib

x = hashlib.md5("foo!")

print x.hexdigest()


#hash is a one way function

#What we can do to make lookup faster.

#https://www.pinterest.com/pin/429953095654195332/