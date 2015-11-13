A = [
 [1, 2, 3],
 [8, 9, 4],
 [7, 6, 5]
]

print A[::-1]  # reverses the whole matrix

print zip(*A[::-1])  # rotates the whole matrix clockwise 90 degree