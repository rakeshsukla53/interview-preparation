__author__ = 'rakesh'


def answer(heights):

    minleft, minright = [], []

    left, right, sum = 0, 0, 0

    for i in range(len(heights)):

        if heights[i] > left:
            left = heights[i]
            minleft.append(left)
        else:
            minleft.append(left)

    for i in (heights[::-1]):

        if i > right:
            right = i
            minright.append(right)
        else:
            minright.append(right)

    minright = minright[::-1]

    for h, l, r in zip(heights, minleft, minright):

        sum += abs(min([l, r])) - h

    return sum

print answer([1, 2, 5, 3, 2])

