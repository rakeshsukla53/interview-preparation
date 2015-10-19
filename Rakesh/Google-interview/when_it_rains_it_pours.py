__author__ = 'rakesh'


def answer(heights):

    row = len(heights)
    col = max(heights)

    newsum = 0

    matrix = [['X' for j in range(i)] for i in heights]

    for i in range(col):

        rainWater = []

        for j in range(row):

            try:

                rainWater.append(matrix[j][i])

            except IndexError:

                rainWater.append('0')

        newsum += ''.join(rainWater).strip('0').count('0')

    return newsum

print answer([6, 1, 2, 3, 7, 4, 6])

