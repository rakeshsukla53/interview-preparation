__author__ = 'rakesh'

def answer(heights):
    minLeft = [0] * len(heights)
    left = 0
    for idx, h in enumerate(heights):
        if left < h:
            left = h
        minLeft[idx] = left

    minRight = [0] * len(heights)
    right = 0
    for idx, h in enumerate(heights[::-1]):
        if right < h:
            right = h
        minRight[len(heights) - 1 - idx] = right

    water = 0
    for h, l, r in zip(heights, minLeft, minRight):
        water += min([l, r]) - h

    return water

print answer([1, 4, 2, 5, 1, 2, 3])

