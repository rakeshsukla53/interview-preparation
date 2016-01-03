
import bisect

a = [5, 2, 6, 1]

print [len(filter(lambda x:x < a[i], a[i+1:])) for i in range(len(a))]

# there are thousands way to do this
# Sort the array
# Use insert sort to find position that will be your number

