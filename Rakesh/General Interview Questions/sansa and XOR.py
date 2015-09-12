__author__ = 'rakesh'

from itertools import combinations

A = [4, 5, 7, 8]
count = 1
for i in range(len(A)):

    for j in range(len(A)):

        if len(A[j:j+count]) == count:

            print A[j:j+count]

    count += 1

#Hacker Rank Problem

