


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

