__author__ = 'rakesh'

def solution(A):
    n = len(A)
    L = [-1] + A
    count = 0
    pos = n // 2
    candidate = L[pos+1]
    for i in xrange(1, n + 1):
        if (L[i] == candidate):
            count = count + 1
    if (count > pos):
        return 1
    return -1


print solution([3,3,4,2])
