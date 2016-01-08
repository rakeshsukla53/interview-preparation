

# This is newton method way to solving the problem

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        X = 1
        while True:
            fx = X*X - x
            if not fx:
                break
            dx = 2*X
            y = X
            X = X - float(fx)/dx

            if str(y) == str(X):
                break

        return int(X)
# time exceeded for this but there is no memory error

print Solution().mySqrt(2)
