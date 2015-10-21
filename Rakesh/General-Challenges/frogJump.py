__author__ = 'rakesh'

def totalJumpsRequired(X, D):
    '''
    calculating total jumps required to cross the river
    :param X:
    :param D:
    :return:
    '''
    totalDistance = X
    totalJumps = X / D
    remainingDistance = totalDistance % D

    if remainingDistance != 0:
        totalJumps += 1

    return totalJumps

def solution(A, X, D):  #X is here the final position

    if D > X: #the frog can jump in one go
        return 0
    if A[0] > D:
        return -1  #the first postion is greater than the maximum distance
    totalJumps = totalJumpsRequired(X, D)
    maxJump = D
    #where the frog at 0th Second
    s = set() #avoid duplicate value
    for i in xrange(len(A)):
        if A[i] <= X:
            s.add(A[i])
        if len(s) == X:
            return i

print solution([1, 3, 1, 4, 2, 5], 7, 3)

























