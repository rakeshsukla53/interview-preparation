
import re
from collections import defaultdict

pattern = re.compile("[a-zA-Z][a-zA-Z]*")

line = raw_input()

result = []
duplicates = defaultdict(int)

for word in pattern.findall(line.lower()):
    result.append("".join(sorted(word)))

result = sorted(result)

for i in result:

    if duplicates.has_key(i):
        pass
    else:
        duplicates[i] += 1
        print i,






