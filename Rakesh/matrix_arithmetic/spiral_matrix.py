

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

        return result

matrix = [
 [],
]

print Solution().spiralOrder(matrix)

'''

There are better ways to solve this problem!

def spiralOrder(self, matrix):
    return matrix and list(matrix.pop(0)) + self.spiralOrder(zip(*matrix)[::-1])



    1, 2, 3

    4, 5, 6

    7, 8, 9

(2). The first row, [1, 2, 3], is used

    4, 5, 6

    7, 8, 9

(3). Rotate the rest into:

    6, 9

    5, 8

    4, 7

(4). Use the first row after rotation. Got [1, 2, 3, 6, 9, ... ] and just keep going !

def spiralOrder(self, matrix):

    result = []

    def helper(mat):
        if mat:
            result.extend(mat[0])
            helper(self.rotate_counter(mat[1:]))

    helper(matrix)
    return result

def rotate_counter(self, mat):
    return zip(*mat)[::-1]

p.s. I isolate the rotation function for readability.
p.s. fixed the redundancy & added a while-loop version under the suggestion of StefanPochmann

def spiralOrder(self, matrix):    #a while-loop version

    result = []

    while matrix:
        result.extend(matrix.pop(0))
        matrix = zip(*matrix)[::-1]    #rotate the remaining matrix counter-clockwise

    return result
'''



