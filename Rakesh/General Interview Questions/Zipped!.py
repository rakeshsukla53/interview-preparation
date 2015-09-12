__author__ = 'rakesh'


inputValues = raw_input().strip().split(' ')

X = int(inputValues[1])

d = dict()

for i in range(X):

    d[i] = raw_input().strip().split(' ')

for i in zip(*[d[i] for i in range(X)]):

    print float(sum(map(float, list(i))))/len(list(i))



