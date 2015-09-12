__author__ = 'rakesh'

from collections import Counter

n = input()
A = raw_input().strip().split(' ')
m = input()
B = raw_input().strip().split(' ')

A = (map(int, A))
B = (map(int, B))

result1 = (Counter(A))
result2 = (Counter(B))

final_result = []

for i in zip(result1.keys(), result1.values()):

    a, b = i

    if result2.has_key(a):

        if result2[a] != b:
            final_result.append(str(a))


print " ".join(final_result)

'''
12
203 204 205 206 207 208 203 204 205 206
13
203 204 204 205 206 207 205 208 203 206 205 206 204
'''
