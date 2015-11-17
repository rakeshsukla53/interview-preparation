

def generator():

    for i in xrange(10000000):
        yield i  # this is basically just like a return object for generator

        # since we are not storing anything in memory we don't take to store anything in a list

        # there is property of yield through which we can store previous values and remembers it

print generator()  # it doesn't store anything in memory if you don't want to use it

# it will return a generator object

def without_generator():
    result = [] # now you need to store value here

    for j in range(1000):
        result.append(j)

    return result

print without_generator()  # this will return the whole list

list.extend()




