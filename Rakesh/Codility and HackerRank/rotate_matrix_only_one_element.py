import collections
def rotateMatrix(matrix, num, rotate_direction):
    for count in range(1):
        temp1 = []
        i = count
        for j in range(count, num - count):
            temp1.append(matrix[i][j])
        j = num - 1 - count
        for i in range(1 + count, num - count - 1):
            temp1.append(matrix[i][j])
        i = num - 1 - count
        for j in range(num - 1 - count, -1 + count, -1):
            temp1.append(matrix[i][j])
        j = count
        for i in range(num - 1 - count - 1, 0 + count, -1):
            temp1.append(matrix[i][j])
        temp = collections.deque(temp1)
        temp.rotate(rotate_direction)
        temp1 = list(temp)
        counter = 0
        i = count
        for j in range(count, num - count):
            matrix[i][j] = temp1[counter]
            counter += 1
        j = num - 1 - count
        for i in range(1 + count, num - count -1):
            matrix[i][j] = temp1[counter]
            counter += 1
        i = num - 1 - count
        for j in range(num - 1 - count, -1 + count, -1):
            matrix[i][j] = temp1[counter]
            counter += 1
        j = count
        for i in range(num - 1 - count - 1, 0 + count, -1):
            matrix[i][j] = temp1[counter]
            counter += 1
        return matrix


if __name__ == '__main__':
    num = int(raw_input())
    matrix = []
    for i in range(num):
        temp = []
        input_string = raw_input().split()
        if len(input_string) != num:
            print 'ERROR'
            exit()
        for element in input_string:
            temp.append(int(element))
        matrix.append(temp)

    matrix_result = rotateMatrix(matrix, num, 1)

    for j in range(num):
        print " ".join(map(str, matrix_result[j]))
