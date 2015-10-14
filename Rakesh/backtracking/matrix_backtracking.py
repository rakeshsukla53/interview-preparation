__author__ = 'rakesh'

#matrix backtracking

matrix = [[1, 1, 0, 0],
  [0, 1, 1, 0],
  [0, 1, 1, 1]]

resultMatrix = [[0, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 0]]


def findPath(matrix, i, j, resultMatrix):

    if i > 2 or j > 3:
        return None

    if matrix[i][j] == 0:
        return None

    if i <= 2 and j <= 3 and matrix[i][j] == 1:
        resultMatrix[i][j] = 1

    if i == 2 and j == 3:
        return resultMatrix

    rowResult = findPath(matrix, i + 1, j, resultMatrix)
    if rowResult:
        return rowResult  #since you are returning result it will only print once if one path is find
    columnResult = findPath(matrix, i, j + 1, resultMatrix)
    if columnResult:
        return columnResult #if you want to print out all the paths then you need to use print because you need to save the result

print findPath(matrix, 0, 0, resultMatrix)




