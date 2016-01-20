

1) Create a matrix to store the coordinates

    (0,0) (0,1) (0,2)

    (1,0) (1,1) (1,2)

    (2,0) (2,1) (2,2)

(2) Read it out using the trick of "Spiral Matrix I"

    (0,0) (0,1) (0,2) (1,2) (2,2) ...

(3) Put 1, 2, 3, ... n**2 at these coordinates sequentially. Done.

def generateMatrix(self, n):

    result = [[0 for i in range(n)] for j in range(n)]
    coord = [[(i,j) for j in range(n)] for i in range(n)]

    count = 1

    while coord:
        for x, y in coord.pop(0):
            result[x][y] = count
            count += 1
        coord = zip(*coord)[::-1]

    return result
