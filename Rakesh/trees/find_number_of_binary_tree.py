__author__ = 'rakesh'


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Check the image for optimized solution and check how we have started with the problem
        #Writing code is the most trivial thing you can imagine

        binarySearchList = list(range(1, n + 2))
        count = []
        count.append(1)
        count.append(1)
        count.append(2)
        for k in range(3, len(binarySearchList)):
            newList = binarySearchList[:k]
            sum = 0
            for i in range(len(newList)):
                leftLength = len(newList[:i])
                rightLength = len(newList[i + 1:])
                #print newList, leftLength, rightLength
                sum += count[leftLength] * count[rightLength]
            count.insert(k, sum)

        return count[n]


