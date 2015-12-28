
import bisect
import decimal

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        bisect.insort(self.data, num)

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if self.data:
            if len(self.data) % 2 == 0:
                mid_position = len(self.data) / 2
                median = (self.data[mid_position] + self.data[mid_position - 1]) / 2.0
            else:
                median = (self.data[len(self.data) / 2])

            return median

# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()
mf.addNum(1)
# mf.addNum(10)
# mf.addNum(2)
print mf.findMedian()

