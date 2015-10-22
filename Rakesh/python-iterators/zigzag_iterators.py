__author__ = 'rakesh'

from itertools import izip_longest

class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v1 = v1
        self.v2 = v2
        self.finalresult = sum([(filter(None, list(i))) for i in izip_longest(self.v1, self.v2)], [])
        self.index = len(self.finalresult)

    def next(self):
        """
        :rtype: int
        """
        return self.finalresult[]



    def hasNext(self):
        """
        :rtype: bool
        """


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())

#The problem with your approach is that it is occupying lots of space which is totally not required

# #class ZigzagIterator(object):
#   def __init__(self, v1, v2):
#     v = [x for v in itertools.izip_longest(v1, v2) for x in v if x!=None][::-1]
#     self.next = v.pop
#     self.hasNext = lambda: bool(v)

#You can also do by the following method


