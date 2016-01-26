
def pramp(arr1, arr2):

   mlogn
   cmp in python
   cmp(array1[i], array2[i]) = 0  +1 -1
   [1, 2, 3]
   [3, 4, 5]

   array1, array2 = sorted(array1), sorted(array2)
   i, j = 0, 0
   result = []
   while i < len(array1) and j < len(array2):
      count = cmp(array[i], array[j])
      if count == 0:
         result.append(array[i])
      if count < 0:
         i += 1
      if count > 0:
         j += 1

   return result

array1 = [1,2,3]
array2 = [1,3,3]

j = 4 or i = 4


function findDuplicates1(Arr1, Arr2):   duplicates = []
   i = 0
   j = 0
   while i < length(Arr1) and j < length(Arr2):
      if Arr1[i] == Arr2[j]:
         duplicated.append(Arr1[i])
         i = i + 1
         j = j + 1
      else if Arr1[i] < Arr2[j]:
         i = i + 1
      else:
         j = j + 1
   return duplicates

#
# >>> a = [1, 2, 3]
# >>> b = [3, 4, 5]
# >>> set(a) & set(b)
# set([3])
# >>>

>>> b = [3, 4, 5]
>>> a = [1, 2, 3]
>>> set(a).intersection(b)
set([3])
>>>

# find common elements

