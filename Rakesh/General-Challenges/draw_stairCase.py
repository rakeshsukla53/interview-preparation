__author__ = 'rakesh'

n = input()

for i in range(1, n + 1):
    for k in range(n - i):
        print '',
    print '#' * i



