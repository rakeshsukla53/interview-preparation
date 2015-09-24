__author__ = 'rakesh'


from itertools import product

for i in product(['G', 'H', 'I'], ['D', 'E', 'F'], ['H', 'I', 'J'], ['H', 'I', 'J'], ['N', 'O', 'P']):

    print "".join(list(i))

#this is the logic
