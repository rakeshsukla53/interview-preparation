__author__ = 'rakesh'

from collections import Counter

def lonelyinteger(a):

    result = Counter(a)

    for i in zip(result.keys(), result.values()):

        k, v = i
        if v == 1:
            return k
if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)

