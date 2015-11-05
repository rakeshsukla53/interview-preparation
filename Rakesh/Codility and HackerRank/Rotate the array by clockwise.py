
row = input()
#column and row will be same here since we are talking about square matrix

matrix = []

for i in range(row):
    col = raw_input().strip().split()
    if row != len(col):
        print "ERROR"
        break
    matrix.append(col)

shifted_matrix = zip(*matrix[::-1])

for j in range(row):
    print " ".join(shifted_matrix[j])

