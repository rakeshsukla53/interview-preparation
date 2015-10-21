__author__ = 'rakesh'

from collections import deque

d = deque('ghi')

print d
d.append('j')
print d
d.appendleft('k')
print d
d.pop()
print d
d.popleft()
print d

#use deque because they are highly efficient
#deque will be mainly used for breadth for search

