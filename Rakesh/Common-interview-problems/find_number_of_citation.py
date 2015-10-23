__author__ = 'rakesh'

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        citations.reverse()
        count = 0

        for i in range(len(citations)):

            if citations[i] > i:
                count += 1

        return count

print Solution().hIndex([3, 0, 6, 1, 5])

