import itertools

a = [[1, 2], [3, 4], [5, 6], [[[[[[100]]]]]]]
print list(itertools.chain.from_iterable(a))


from itertools import chain

B = [[1, 2], [3, 4]]

print sum(B, [])
print list((chain.from_iterable(B)))



