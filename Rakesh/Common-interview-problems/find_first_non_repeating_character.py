__author__ = 'rakesh'

from collections import OrderedDict

def nonRepeated(s):

    result = OrderedDict()

    for i in s:
        if result.has_key(i):
            result[i] += 1
        else:
            result[i] = 1

    return sorted(result.items(), key=lambda t: t[1])[0][0]

nonRepeated('mnonmpsms')
