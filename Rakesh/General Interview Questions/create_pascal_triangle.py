
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        if numRows = 5
               [
                     [1],
                    [1,1],
                   [1,2,1],
                  [1,3,3,1],
                 [1,4,6,4,1]
               ]
        """

        num = [[1], [1, 1]]
        if numRows == 1:
            return num[0]
        elif numRows == 2:
            return num

        row = []
        for i in range(2, numRows):
            for j in range(i - 1):
                row.append(sum(num[-1][j:j + 2]))
            num.append([1] + row + [1])
            row = []

        return num
