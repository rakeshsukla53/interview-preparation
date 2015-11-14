
# what is the need of Global Interpreter Lock in Python

 The Python interpreter is not fully thread-safe. In order to support multi-threaded Python programs, there’s a global lock, called the global interpreter lock or GIL, that must be held by the current thread before it can safely access Python objects. Without the lock, even the simplest operations could cause problems in a multi-threaded program: for example, when two threads simultaneously increment the reference count of the same object, the reference count could end up being incremented only once instead of twice.

# python programs will never result in segmentation fault only because safe operations are permitted

In other words, the GIL is prevents corruption of state. Python programs should never produce a segmentation fault, because only memory safe operations are permitted. The GIL extends this assurance to multi-threaded programs.

