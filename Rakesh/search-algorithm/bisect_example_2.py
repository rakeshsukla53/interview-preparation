# File: bisect-example-2.py

import bisect

list = [10, 20, 30]

print list
print bisect.bisect(list, 25)
print bisect.bisect(list, 15)

## $ python bisect-example-2.py
## [10, 20, 30]
## 2
## 1
