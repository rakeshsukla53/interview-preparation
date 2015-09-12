__author__ = 'rakesh'

#Take hint from these comments http://stackoverflow.com/questions/25750240/how-to-find-pairs-with-product-greater-than-sum


from itertools import combinations

def C(n, A, B):

    return A[n] + float(B[n]) / 1000000

def solution(A, B):

    count = 0

    for i in combinations(list(range(1, len(A))), 2):

        P, Q = i
        if C(P, A, B)*C(Q, A, B) >= C(P, A, B) +C(Q, A, B):
            print i

            count += 1

    return count

print solution([0, 1, 2, 2, 3, 5], [500000, 500000, 0, 0, 0, 20000])
