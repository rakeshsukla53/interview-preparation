
import bisect

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        first_row = matrix[0]
        row_size = len(matrix)
        i = bisect.bisect_left(first_row, target)
        print i
        if i != len(first_row) and first_row[i] == target:
            return True
        else:
            for p in range(i - 1, -1, -1):
                for k in range(1, row_size):
                    if matrix[k][p] == target:
                        return True

        return False

matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

print Solution().searchMatrix(matrix, 18)


