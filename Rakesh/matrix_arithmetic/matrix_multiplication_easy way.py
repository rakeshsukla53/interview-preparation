
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """

        return[[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*B)] for X_row in A]

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0, 0 ],
  [ 0, 0, 0, 0 ],
  [ 0, 0, 1, 0 ]
]


print Solution().multiply(A, B)

