class Solution(object):

    __totalCost = -1
    __costs = None

    def paintHouses(self,  start, color, currentCost):
        currentCost += self.__costs[start][color]

        # optimization
        if self.__totalCost != -1 and currentCost > self.__totalCost:
            return

        if start + 1 < len(self.__costs):
            nextColor1 = (color + 1) % 3
            nextColor2 = (color + 2) % 3
            self.paintHouses(start + 1, nextColor1, currentCost)
            self.paintHouses(start + 1, nextColor2, currentCost)
        else:
            if self.__totalCost == -1 or currentCost < self.__totalCost:
                self.__totalCost = currentCost

    def minCost(self, costs):
        self.__costs = costs
        if len(costs) == 0:
            return 0
        """
        :type costs: List[List[int]]
        :rtype: int
        """

        # paints first house with all colors
        self.paintHouses(0, 0, 0)
        self.paintHouses(0, 1, 0)
        self.paintHouses(0, 2, 0)

        return self.__totalCost


costs = [[1, 4, 2], [0, 15, 18], [1, 250, 100], [100, 19, 20]]

print Solution().minCost(costs)

