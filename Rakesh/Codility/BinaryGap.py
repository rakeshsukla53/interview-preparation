__author__ = 'rakesh'

def solution(N):
    # write your code in Python 2.7
    import re
    t = [m.start() for m in re.finditer('1', bin(N).split('b')[1])]
    if t is None or len(t) == 1:
        return 0
    else:
        return max([j - i for i, j in zip(t[:-1], t[1:])]) - 1

print solution(529)




