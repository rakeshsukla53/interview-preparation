
import bisect

def find_eq(seq):


    i = bisect.bisect_left(seq, i, lo=0, hi=)

print find_eq([-8, 0, 2, 5])


def find_eq(seq):

   i,j=0,len(seq)-1
   while i<=j:
      mid = (i+j)//2
      if seq[mid] == mid:
         return mid
      else:
         if seq[mid] > mid:
            j=mid-1
         else:
            i=mid+1
   return -1