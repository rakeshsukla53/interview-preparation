
from itertools import repeat

s = [1, 2, 3]

s.append(4)
# s.extend(5)  # extend is basically to append iterable object. it will show an error here

s.append('abc')  # it will append complete list 'abc'
s.extend('def')  # it will iterate through 'def' and then add to the list

# s.extend('def') -->   [ s.append(i) for i in 'def']

print s

print list(repeat('A', 3))

