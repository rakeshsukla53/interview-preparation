__author__ = 'rakesh'


#fibonacii series using memoization

def fibo(n, computed = {0:1, 1:1}):

    if n not in computed:

        computed[n] = fibo(n-1, computed) + fibo(n-2, computed)

    return computed[n]


print fibo(900)  #if you want to know the fibonacii series of such large number


#but the problem there is you don't know how many times you will execute it.
