
from collections import defaultdict

row = input()
matrix = []
duplicates = defaultdict(list)

for i in range(row):
    col_val = raw_input().strip().split()
    col = len(col_val)
    matrix.append(col_val)

k = input()

for row_idx in range(row):
    for col_idx in range(col):
        if duplicates.has_key(matrix[row_idx][col_idx]):
            a, b = duplicates[matrix[row_idx][col_idx]]
            if abs(row_idx - a) + abs(b - col_idx) == k:
                print "YES"
                exit()
        else:
            duplicates[matrix[row_idx][col_idx]] = [row_idx, col_idx]

print 'NO'
