
def solution(X, A):

    for i in range(1, len(A)):

        x = len(filter(lambda x: x == X, A[:i]))

        y = len(filter(lambda x: x != X, A[i:]))

        if x == y:
            return i

print solution(5, [5, 5, 1, 7, 2, 3, 5])

