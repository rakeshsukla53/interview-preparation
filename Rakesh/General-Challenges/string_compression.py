__author__ = 'rakesh'

from collections import defaultdict
characterCounter = defaultdict(int) #for counting the frequency
inputString = raw_input()
finalResult = []
for i in range(len(inputString)):
    characterCounter[inputString[i]] += 1
    if i == len(inputString) - 1:
        finalResult.append(inputString[i])
        finalResult.append(str(characterCounter[inputString[i]]))
        break
    if inputString[i] != inputString[i+1]:
        finalResult.append(inputString[i])
        finalResult.append(str(characterCounter[inputString[i]]))
        characterCounter.pop(inputString[i])
    else:
        pass

finalResult = filter(lambda x: x != '1', finalResult)

print "".join(finalResult)
