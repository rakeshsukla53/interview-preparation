l = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721, 129140163, 387420489, 1162261467,486784401, 10460353203]

def findCombination(value):

    for i in range(len(l)):

        if sum(l[:i]) > value:

           return len(l[:i])


def findIndex(step, value):

    index = ((pow(3, step)) - 1)/2

    rowValue = (int((value + index)/pow(3, step))) % 3

    return rowValue

def answer(value):

    totalSteps = (findCombination(value))

    pattern = ['-', 'R', 'L']

    finalResult = []

    try:
        for i in xrange(totalSteps):

            resultIndex = (findIndex(i, value))

            finalResult.append(pattern[resultIndex])

    except TypeError as e:
        pass

    return finalResult

print answer(1000000000)








