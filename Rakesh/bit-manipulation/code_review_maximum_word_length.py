from itertools import combinations


class Solution(object):


    def dis_joint(self, word1, word2):
        return not (set(word1) & set(word2))

    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        max_product = 0
        words = sorted(words, key=len, reverse=True)
        for w1, w2 in combinations(words, 2):
            if self.dis_joint(w1, w2):
                pass

            if (len(w1) in (len(w2), len(w2) + 1) and

            # the whole if condition can be written here

Solution().maxProduct(["eae", "ea", "aaf", "bda", "fcf", "dc", "ac", "ce", "cefde", "dabae"])

# >>> a = 'cefde'
# >>> b = 'dabae'
# >>> c = 'klmd'
# >>> set(a) & set(b)
# set(['e', 'd'])
# >>> set(a) & set(c)
# set(['d'])
# >>> set(a) - set(b)
# set(['c', 'f'])
# >>>

# if you should use this technique to figure out the if the words contain any common letters




