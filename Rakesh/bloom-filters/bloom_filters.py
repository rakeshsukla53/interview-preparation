__author__ = 'rakesh'

import pyblume

BLOOM_FILTER_MAX_FILESIZE = 1024 * 1024 * 500
BLOOM_ERROR_RATE = 0.000001
fileloc = "/tmp/test.blume"

bf = pyblume.Filter(BLOOM_FILTER_MAX_FILESIZE, BLOOM_ERROR_RATE, fileloc)

for i in range(313):

    bf.add(str(i))

bf.close()

check = [str(j) for j in range(300, 400)]

print check

bf = pyblume.open(fileloc, for_write=False)
for x in check:
    if x in bf:
        print "Found"
bf.close()

'''
NOTES:

Bloom Filters Description - https://www.pinterest.com/pin/429953095654194981/

https://www.pinterest.com/pin/429953095654194979/

'''

