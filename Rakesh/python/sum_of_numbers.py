__author__ = 'rakesh'

def answer(x):

    y = str(x)

    s = map(int, y)

    sumNumbers = sum(s)

    if len(str(sumNumbers)) == 1:

        return sumNumbers

    else:

        return answer(sumNumbers)



