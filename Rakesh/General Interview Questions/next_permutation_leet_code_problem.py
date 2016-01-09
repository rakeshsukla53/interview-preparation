

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        inputString = "".join(map(str, nums))
        stringNumbers = map(ord, inputString)
        finalList = []
        if len(inputString) <= 1:
            nums.sort()

        else:
            for k in xrange(len(stringNumbers) - 1, -1, -1):

                if stringNumbers[k] <= stringNumbers[k - 1]:
                    continue
                else:
                    swapValue = stringNumbers[k - 1]
                    prefix = stringNumbers[:k]

                    if len(prefix) == 0:
                        break

                    for f in xrange(len(stringNumbers) - 1, -1, -1):
                        if stringNumbers[f] > swapValue:
                            index = f
                            break

                    stringNumbers[k - 1], stringNumbers[index] = stringNumbers[index], stringNumbers[k-1]
                    suffix = stringNumbers[k:]
                    prefix = stringNumbers[:k]
                    suffix.reverse()
                    finalList = prefix + suffix
                    break

            if "".join(map(chr, finalList)) == inputString or len(finalList) == 0:
                nums.sort()

            else:
                nums = map(int, map(chr, finalList))
                print nums

Solution().nextPermutation([1, 2])

