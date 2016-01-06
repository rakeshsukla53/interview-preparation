
from itertools import groupby

data = [2, 1, 2, 2, 2]

for k, g in groupby(data, lambda x: x == 2):
    if k:
        print list(g)

from itertools import groupby

data = 'AAABBBCCCDDDDDDEEEEEEEEEEEEE'

max_length, character = 0, ''

for k, g in groupby(data):
    if k:
        group = list(g)
        if len(group) > max_length:
            max_length = len(group)
            character =
print max_length, character

from collections import Counter
from itertools import groupby

data = ["eat", "tea", "tan", "ate", "nat", "bat"]


