__author__ = 'rakesh'

def binarySearch(alist, item):

    #for binary search I am assuming that the list is increasing order

    mid = len(alist) / 2

    if item == alist[mid]:

        return 'Item Found'

    if mid == 0:
        return 'Item not Found'

    if item > alist[mid]:

        return binarySearch(alist[mid+1:], item)

    else:

        return binarySearch(alist[0:mid], item)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binarySearch(testlist, 17))
print(binarySearch(testlist, 2))
print(binarySearch(testlist, 100))

