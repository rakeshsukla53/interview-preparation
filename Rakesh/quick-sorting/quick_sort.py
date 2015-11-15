# the best part of this algorithm in place quicksort

# most of the algorithms written for sorting are quick sort since it doesn't take any extra space. But in Python the algorithm used is tim sort which is a mixture of merge sort and insertion sort.

# we choose a pivot which is middle of the value

def partition(A, start, end):
    pivot = A[end]
    pindex = start
    for i in range(start, end):
        if A[i] <= pivot:
            A[i], A[pindex] = A[pindex], A[i]
            pindex += 1

    A[pindex], A[end] = A[end], A[pindex]
    return pindex

def quick_sort(A, start, end):

    if start < end:
        pindex = partition(A, start, end)
        quick_sort(A, start, pindex - 1)
        quick_sort(A, pindex + 1, end)

    return A

print quick_sort([10, 1, 2, 1, 1, 1], 0, 5)

