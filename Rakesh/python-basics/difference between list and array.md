# LIST 

Basically, Python lists are very flexible and can hold completely heterogeneous, arbitrary data, and they can be appended to very efficiently, in amortized constant time. If you need to shrink and grow your array time-efficiently and without hassle, they are the way to go. But they use a lot more space than C arrays.

# ARRAY 

The array.array type, on the other hand, is just a thin wrapper on C arrays. It can hold only homogeneous data, all of the same type, and so it uses only sizeof(one object) * length bytes of memory. Mostly, you should use it when you need to expose a C array to an extension or a system call (for example, ioctl or fctnl). It's also a good way to represent a mutable string (array('B', bytes)) until that actually becomes available in Python 3.0.

However, if you want to do math on a homogeneous array of numeric data, then you're much better off using NumPy, which can automatically vectorize operations on complex multi-dimensional arrays.

To make a long story short: array.array is useful when you need a homogeneous C array of data for reasons other than doing math.
