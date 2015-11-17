

# what is the difference between range and xrange, and how is changed over the years.

    In [1]: range(5)
    
    Out[1]: [0, 1, 2, 3, 4]
    
    
    In [2]: xrange(5)
    
    Out[2]: xrange(5)
    
    
    In [3]: print xrange.__doc__
    
    xrange([start,] stop[, step]) -> xrange object
    
    
    Like range(), but instead of returning a list, returns an object that
    
    generates the numbers in the range on demand.  For looping, this is 
    
    slightly faster than range() and more memory efficient.
    
# xrange is a generator and it will only generate when you demand from it. Range will give you a list 

