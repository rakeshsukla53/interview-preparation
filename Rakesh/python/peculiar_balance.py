
import itertools

l = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721, 129140163]

def findCombination(value):

    for i in range(len(l)):

        if sum(l[:i]) > value:

           return len(l[:i])

def R(r):

    rightWeight = 0

    for i in xrange(len(r)):
        rightWeight += l[r[i]]

    return rightWeight

def L(k, x):

    leftWeight = x

    for j in xrange(len(k)):
        leftWeight += l[k[j]]

    return leftWeight


def indices(mylist, value):
    return [i for i, x in enumerate(mylist) if x==value]


def answer(x):

    pattern = ['R', 'L', '-']
    patternLength = findCombination(x)

    for p in itertools.product(pattern, repeat=patternLength):  #So I am actually looking for catersian product

        left = R(indices(list(p), 'R'))

        right = L(indices(list(p), 'L'), x)

        if left == right:

            print list(p)
            break

        else:
            pass

answer(1000000)

