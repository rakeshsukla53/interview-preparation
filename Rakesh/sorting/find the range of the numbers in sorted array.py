
import bisect

A = [0.5, 0.6, 0.7, 1, 10, 12, 13, 14]

print [bisect.bisect_left(A, 1), bisect.bisect_right(A, 1) - 1]






