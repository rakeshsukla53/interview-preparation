class Solution(object):
    def maxProduct(self, words):
        """
        maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters
        >> maxProduct(["eae", "ea", "aaf", "bda", "fcf", "dc", "ac", "ce", "cefde", "dabae"])
        >> 16
        """
        max_product = 0
        words = sorted(words, key=len, reverse=True)
        for index, j in enumerate(words):
            for i in words[index + 1:]:
                count = 0
                for k in i:
                    if k in j:
                        count = 1
                        break
                if not count:
                    m = len(j)
                    n = len(i)
                    word_product = m * n
                    if ((m == n) or (m > n and n == m - 1)) and word_product > max_product:
                        return word_product
                    if word_product > max_product:
                        max_product = word_product
        return max_product

print Solution().maxProduct(["eae", "ea", "aaf", "bda", "fcf", "dc", "ac", "ce", "cefde", "dabae"])


