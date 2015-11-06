
def solution(X, A):

    not_equal_value = 0
    equal_value = 0

    for i in range(len(A)):
        if X != A[i]:
            not_equal_value += 1

    for j in range(len(A)):
        if not_equal_value == equal_value:
            return j
        if X == A[j]:
            equal_value += 1
        else:
            not_equal_value -= 1
