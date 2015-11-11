
user_input = map(int, raw_input().strip().split(' '))

import math

def find_all_combination(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

M, N = user_input[0], user_input[1]

print find_all_combination(M, N)

# count = 0

# coins = ['T'] * M
#
# for i in range(N):
#     coins[i] = 'H'
#
# a = list(perm_unique(coins))
# print len(a)






