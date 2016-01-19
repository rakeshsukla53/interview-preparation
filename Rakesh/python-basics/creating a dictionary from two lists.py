from itertools import izip

names = ['raymond', 'rachel', 'matthew', 'rakesh']
colors = ['blue', 'green', 'blue']

d = dict(izip(names, colors))

print d

