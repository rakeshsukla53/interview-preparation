__author__ = 'rakesh'

def answer(heights):

    sum = 0

    if len(heights) == 1 or len(heights) == 2:

        return None

    else:
        for i in range(len(heights)-2):

            middle = heights[i+1]

            minleft = max(heights[0:i+1])
            minright = max(heights[i+2:])

            if middle <= minleft and middle <= minright:
                sum += abs(min(minleft, minright) - middle)

        return sum

print answer([1, 5, 3, 2, 5, 3, 6, 9, 1, 10])
