__author__ = 'rakesh'

i = 5
j = 6

def sink(i, j):

    if i > 0 and j > 0:
        print "Rakesh"
        map(sink, (i + 1, i - 1, i), (j + 1, j - 1, j + 2))

sink(i, j)

