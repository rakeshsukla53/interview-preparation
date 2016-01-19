
from itertools import izip

for name, color in zip(list1, list2):
    print name, color

# but izip is better

for name, color in izip(list1, list2)

