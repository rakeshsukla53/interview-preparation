

import bisect

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for index, row in enumerate(matrix):
            i = bisect.bisect_left(row, target)
            if row[0] > target:
                break
            try:
                if matrix[index][i] == target:
                    return True
            except IndexError:
                pass
        return False

matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

print Solution().searchMatrix(matrix, 8)


# def searchMatrix(self, matrix, target):
#     return any(target in row for row in matrix)

# this the best method
'''
We start search the matrix from top right corner, initialize the current position to top right corner, if the target is greater than the value in current position, then the target can not be in entire row of current position because the row is sorted, if the target is less than the value in current position, then the target can not in the entire column because the column is sorted too. We can rule out one row or one column each time, so the time complexity is O(m+n).
'''

