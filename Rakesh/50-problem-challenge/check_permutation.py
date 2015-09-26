__author__ = 'rakesh'

from collections import defaultdict

def solution(A):
    '''
    :param A: It is an list
    :return: return 1 if it is an permutation otherwise zero
    '''
    hashPerm = defaultdict(int)

    if len(A) < 1:
        return 0

    for i in range(0, len(A)):
        hashPerm[A[i]] = ''  #this whole operation will take n time

    for k in range(1, len(A)+1):  #checking whether the number will be there
        if not hashPerm.has_key(k):
            return 0

    return 1




