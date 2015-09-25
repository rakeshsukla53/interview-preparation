__author__ = 'rakesh'

def solution(A):
    # write your code in Python 2.7
    p, q, r = [], [], []
    finalResult = []
    if len(A) < 3:
        return -1  #no triplet exists
    for i in range(len(A)-1):
        if A[i] > A[i+1]:
            p.append(i)
        if A[i] < A[i+1]:
            q.append(i)

    q = filter(lambda x: x > p[0], q)

    print p, q

solution([0, 1, 3, -2, 0, 1, 0, -3, 2, 3])

