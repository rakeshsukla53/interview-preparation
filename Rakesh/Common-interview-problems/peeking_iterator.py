__author__ = 'rakesh'

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.arrayValue = iterator
        self.count = 0

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.arrayValue[self.count+1]

    def next(self):
        """
        :rtype: int
        """
        self.count += 1
        return self.arrayValue[self.count]

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.count == len(self.arrayValue)-1:
            return False
        else:
            return True

#Your PeekingIterator object will be instantiated and called as such:
iter = PeekingIterator([0,1,1,2,2,1,1,2,0,1,0,2,0])
while iter.hasNext():
    val = iter.peek()   # Get the next element but not advance the iterator.
    iter.next()         # Should return the same value as [val].
