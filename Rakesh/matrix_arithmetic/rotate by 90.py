

a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

print a

# rotate by 90 degree
print [list(i) for i in (zip(*a[::-1]))]

# transpose
print [list(i) for i in (zip(*a))]

'''
1 2 3 4             9   5  1
5 6 7 8             10  6  2
9 10 11 12          11  7  3
                    12  8  4print [list(i) for i in (zip(*a[::-1]))]
'''


