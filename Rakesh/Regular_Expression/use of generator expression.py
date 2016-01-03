
from itertools import product
from string import *

keywords = (''.join(i) for i in product(ascii_letters + digits, repeat=3))


# this is a generator expression to avoid holding all the strings in memory.
print keywords





