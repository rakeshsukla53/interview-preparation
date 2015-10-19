__author__ = 'rakesh'

def answer(str_S):

    d = {0: 1, 1: 1, 2: 2}
    str_S = int(str_S)
    i = 1
    while True:

        if i > 1:
            d[i*2] = d[i] + d[i+1] + i
            if d[i*2] == str_S:
                return i*2
            elif d[i*2] > str_S:
                return None

        if i>=1:
            d[i*2+1] = d[i-1] + d[i] + 1
            if d[i*2+1] == str_S:
                return i*2 + 1
            elif d[i*2+1] > str_S:
                return None

        i += 1

print answer('121313232323237240724232749324232323249247283023828248')

#This program right now is neither memory optimized or algorithmically correct
#this method is not suitable , there is no way it can be done in this method!
#this method is also not scalable

'''
def fib(n, computed = {0: 0, 1: 1}):

    if n not in computed:

        computed[n] = fib(n-1, computed) + fib(n-2, computed)

    return computed[n]

print fib(10)
'''
