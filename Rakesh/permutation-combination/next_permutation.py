__author__ = 'rakesh'

n = input()

for i in range(n):

    inputString = list(raw_input().strip())
    stringNumbers = map(ord, inputString)
    finalList = []
    if len(inputString) <= 1:

        print 'no answer'

    else:
        for k in xrange(len(stringNumbers)-1, -1, -1):

            if stringNumbers[k] <= stringNumbers[k-1]:
                continue

            else:
                swapValue = stringNumbers[k-1]
                prefix = stringNumbers[:k]

                if len(prefix) == 0:
                    break

                for f in xrange(len(stringNumbers)-1, -1, -1):
                    if stringNumbers[f] > swapValue:
                        index = f
                        break

                stringNumbers[k-1], stringNumbers[index] = stringNumbers[index], stringNumbers[k-1]
                suffix = stringNumbers[k:]
                prefix = stringNumbers[:k]
                suffix.reverse()
                finalList = prefix + suffix
                break

        if "".join(map(chr, finalList)) == inputString or len(finalList) == 0:
            print "no answer"

        else:
            print "".join(map(chr, finalList))

