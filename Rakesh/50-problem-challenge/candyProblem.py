__author__ = 'rakesh'

#we will move two ways one is right and other is left and then take the max of it
#candy problem

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        tempA = [1] * len(ratings)

        for i in range(len(ratings) - 1):
            if ratings[i] > ratings[i + 1]:
                tempA[i] = tempA[i + 1] + 1
            elif ratings[i + 1] > ratings[i]:
                tempA[i + 1] = tempA[i] + 1

        for j in range(len(ratings) - 1, 0, -1):
            if ratings[j - 1] > ratings[j]:
                if tempA[j - 1] > tempA[j]:
                    pass
                else:
                    tempA[j - 1] = tempA[j] + 1

            elif ratings[j] > ratings[j - 1]:
                if tempA[j] > tempA[j - 1]:
                    pass
                else:
                    tempA[j] = tempA[j - 1] + 1

        print sum(tempA)

#Solution().candy([10, 3, 10, 5, 1, 10])
