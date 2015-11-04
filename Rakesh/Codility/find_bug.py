#Regarding Problem 2

If you look at problem 2, you can easily predict that this is some code for binary search since you are also expecting worst case complexity to be O(logn). There are various ways a binary search can be written:

1 - Using bit manipulation
2 - Using depth for search
3 - Simple Iteration

This problem looks like an iterative solution of Binary Search.

Solution:

    def solution(A, X):
        N = len(A)
        if N == 0:
            return -1
        l = 0
        r = N - 1
        while l <= r:
            m = (l + r) // 2
            if A[m] == X:
                return m
            if A[m] > X:
                r = m - 1
            else:
                l = m + 1
        return -1

Now if you try to debug the program you have to change at most 4 lines to pass all the test cases, when i just update 3 lines but it was not clearing every test case. I may be wrong here but to make sure all the test cases are passed we need to modify at least 4 lines. I won't mind if you reject me at this stage, will be very happy to know the right solution.