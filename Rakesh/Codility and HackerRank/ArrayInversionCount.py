# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            return midpoint
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

def solution(A):

    B = list(A)
    B.sort()
    inversion_count = 0
    for i in range(len(A)):
        j = binarySearch(B, A[i])
        while B[j] == B[j - 1]:
            if j < 1:
                break
            j -= 1

        inversion_count += j
        B.pop(j)

    if inversion_count > 1000000000:
        return -1
    else:
        return inversion_count

print solution([4, 10, 11, 1, 3, 9, 10])










