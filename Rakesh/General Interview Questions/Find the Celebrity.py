
# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

# find a celebrity question

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """

        for i in range(n):
            count = 0
            for j in range(n):
                if not i == j:
                    if not knows(i, j) and knows(j, i):
                        celebrity = i
                        count += 1
                    else:
                        break

            if count == n - 1:
                return celebrity

        return -1


