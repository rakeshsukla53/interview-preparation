
import bisect

list = [10, 20, 30]

bisect.insort(list, 25)
bisect.insort(list, 15)

print list

## $ python bisect-example-1.py
## [10, 15, 20, 25, 30]


