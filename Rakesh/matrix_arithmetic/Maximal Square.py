from itertools import groupby

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        nrows = len(matrix)
        ncols = len(matrix[0])
        area_largest_square = 0

        for i in range(nrows - 1):
            square_size = 2     # minimum size of the square
            result = matrix[i]
            count = False
            for j in range(i + 1, nrows):
                result = [int(result[k]) + int(matrix[j][k]) for k in range(ncols)]

                for k, g in groupby(result, lambda x: x == square_size):
                    if k:
                        if len(list(g)) >= square_size:
                            if square_size > area_largest_square:
                                area_largest_square = square_size

                            square_size += 1
                            count = True
                            break

                if not count:
                    break

        return pow(area_largest_square, 2)


print Solution().maximalSquare([[1, 1, 1, 1, 1], [1, 1, 1, 1, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 1]])


