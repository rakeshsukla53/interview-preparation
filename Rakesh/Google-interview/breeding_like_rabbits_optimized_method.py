__author__ = 'rakesh'

#here we have to know about memoization

#Idea 1 - To sabe the result in some variables ---but it is not feasible. Fibonacci can be done since only two variables
#are required. Also in the memoization part there is only recursion process not all.

#Idea 2 - Use some kind of hash table here, but it will occupy lots of memory. Chances of memory error

#Idea 3 - For this type of problem if you have do memoization through recursion


#Idea 4 - if there is no base condition then there is no way a recursion can happen and the base condition should keep on decreasing

#Idea 5 -






'''
Yes. The primitive recursive solution takes a lot of time. The reason for this is that for each number calculated, it needs to calculate all the previous numbers more than once. Take a look at the following image.

Tree representing fibonacci calculation

It represents calculating Fibonacci(5) with your function. As you can see, it computes the value of Fibonacci(2) three times, and the value of Fibonacci(1) five times. That just gets worse and worse the higher the number you want to compute.

What makes it even worse is that with each fibonacci number you calculate in your list, you don't use the previous numbers you have knowledge of to speed up the computation – you compute each number "from scratch."

There are a few options to make this faster:
1. Create a list "from the bottom up"

The easiest way is to just create a list of fibonacci numbers up to the number you want. If you do that, you build "from the bottom up" or so to speak, and you can reuse previous numbers to create the next one. If you have a list of the fibonacci numbers [0, 1, 1, 2, 3], you can use the last two numbers in that list to create the next number.

This approach would look something like this:

>>> def fib_to(n):
...     fibs = [0, 1]
...     for i in range(2, n+1):
...         fibs.append(fibs[-1] + fibs[-2])
...     return fibs
...

Then you can get the first 20 fibonacci numbers by doing

>>> fib_to(20)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]

Or you can get the 17th fibonacci number from a list of the first 40 by doing

>>> fib_to(40)[17]
1597

2. Memoization (relatively advanced technique)

Another alternative to make it faster exists, but it is a little more complicated as well. Since your problem is that you re-compute values you have already computed, you can instead choose to save the values you have already computed in a dict, and try to get them from that before you recompute them. This is called memoization. It may look something like this:

>>> def fib(n, computed = {0: 0, 1: 1}):
...     if n not in computed:
...         computed[n] = fib(n-1, computed) + fib(n-2, computed)
...     return computed[n]

This allows you to compute big fibonacci numbers in a breeze:

>>> fib(400)
176023680645013966468226945392411250770384383304492191886725992896575345044216019675
'''










