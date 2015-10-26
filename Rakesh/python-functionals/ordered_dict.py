__author__ = 'rakesh'

from collections import OrderedDict

A = [1,2,3,4,5]

my_dictionary = OrderedDict()

for i in A:
    my_dictionary[i] = ''

print my_dictionary

print my_dictionary.keys()

print my_dictionary.values()

#here you can maintain the order easily using Ordered Dict


