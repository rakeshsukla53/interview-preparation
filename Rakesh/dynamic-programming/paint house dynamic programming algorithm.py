
class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # total number of houses
        n = len(costs)
        if n < 1:
            return None
        elif n == 1:
            return min(costs[0])

        # calculate mininum cost to paint the house
        for i in range(1, n):
            costs[i][0] = min(costs[i - 1][1] + costs[i][0], costs[i - 1][2] + costs[i][0])
            costs[i][1] = min(costs[i - 1][0] + costs[i][1], costs[i - 1][2] + costs[i][1])
            costs[i][2] = min(costs[i - 1][0] + costs[i][2], costs[i - 1][1] + costs[i][2])

        return min(costs[n - 1])


print Solution().minCost([[1, 4, 2], [0, 15, 18], [1, 250, 100], [100, 19, 20]])

