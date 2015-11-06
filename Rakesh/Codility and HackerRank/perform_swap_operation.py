
import bisect

def find_ge(a, x):
    'Find leftmost value greater than x'
    i = bisect.bisect_right(a, x)
    return i

def solution(A):

    if A is None:
        return False

    for i in range(len(A) - 1):

        if A[i] > A[i + 1]:

            if i + 2 == len(A):
                return True
            swap_index = find_ge(A, A[i])
            A[swap_index - 1], A[i] = A[i], A[swap_index - 1]
            break

    print A

    for j in range(len(A) - 1):

        if A[j] > A[j + 1]:
            return False

    return True

