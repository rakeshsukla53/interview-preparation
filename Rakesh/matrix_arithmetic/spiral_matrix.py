

# run time of my solution beat 80% of submission


from collections import deque

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        nrows = deque()
        ncols = deque()
        nrows.extend(range(len(matrix)))
        ncols.extend(range(len(matrix[0])))
        result = []

        while True:

            if not ncols or not nrows:
                break

            row = ncols[0]
            for i in ncols:  # go over the row
                result.append(matrix[row][i])
            nrows.popleft()  # since row is traversed, remove it

            if not ncols or not nrows:
                break

            col = ncols[-1]
            for j in nrows:
                result.append(matrix[j][col])
            ncols.pop()  # the entire col has been traversed

            if not ncols or not nrows:
                break

            row = nrows[-1]
            ncols.reverse()
            for k in ncols:  # now moving backwards
                result.append(matrix[row][k])
            nrows.pop()  # the entire last row is traversed
            ncols.reverse()

            if not ncols or not nrows:
                break

            col = ncols[0]
            nrows.reverse()
            for p in nrows:
                result.append(matrix[p][col])
            ncols.popleft()
            nrows.reverse()

            if not ncols or not nrows:
                break

        return result

matrix = [
 [],
]

print Solution().spiralOrder(matrix)
