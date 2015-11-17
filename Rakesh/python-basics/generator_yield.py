
import time
from memory_profiler import profile
startT = time.time()
# print startT


# range will destroy your processor, always use generator which will yield if you want to survive

# for i in range(100000000):
#
#     pass
#
# print time.time() - startT

@profile
def func():
    for i in xrange(100):  #

        print i

    print time.time() - startT

if __name__ == '__main__':
    func()
