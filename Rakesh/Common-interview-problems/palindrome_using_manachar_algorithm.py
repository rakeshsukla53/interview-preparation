__author__ = 'rakesh'

#find the lonest palindrome sequence

def solution(A):

    totalSum = sum(A)
    firstSum = 0
    count = 0
    for i in range(len(A)):

        if i == 0:
            if totalSum - A[i] == 0:
                count = 1
                return i
        if i >= 1:
            firstSum += A[i-1]
            if firstSum == totalSum - firstSum - A[i]:
                count = 1
                return i

    if count == 0:
        return -1

print solution([-1, 3, 4, 5, 1,6])