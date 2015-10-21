__author__ = 'rakesh'

def solution(A):
    '''
    :param A: it is an list
    :return: whether there exists any triplet where the triangle can be formed
    '''
    if len(A) < 3:
        return 0
    A.sort() #this will take nlogn
    p, q, r = 0, 0, 0
    for i in range(len(A) - 2): #this will take n time
        p = i
        q = i + 1
        r = i + 2
        if (A[p] + A[q] > A[r]) and (A[p] + A[r] > A[q]) and (A[r] + A[q] > A[p]):
            return 1
        else:
            pass

    return 0

print solution([10, 2, 5, 3, 1, 8, 20])






