
# updating state variables

def fibonacii(n):
    x, y = 0, 1
    for i in range(n):
        print x
        y, x = x + y, y

# this is how you update the state variables
# ordering also doesn't matter here
# easy to find the errors

fibonacii(10)

# don't underestimate the advantageous of updating state variables at the same time. It eliminates the entire class of errors due to out of orders updates. it allows high level thinking : chunking

