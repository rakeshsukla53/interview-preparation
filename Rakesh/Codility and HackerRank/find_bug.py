
def binarySearch(A, x):
    n = len(A)
    beg = 0
    end = n - 1
    result = -1
    while (beg <= end):
        mid = (beg + end) / 2
        if (A[mid] <= x):
            beg = mid + 1
            l = mid
        else:
             end = mid - 1
    if A[l] == x:
        return l
    return result

print binarySearch([1, 2, 3, 4, 5, 6], 2)

