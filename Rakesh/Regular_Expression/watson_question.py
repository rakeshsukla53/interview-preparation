__author__ = 'rakesh'

watson = 'watson  Represents|watson represents|Watson represents a first step into cognitive systems, a new era of computing.|first step into  Cognitive|Cognitive Systems; a new era|what does watson represent'

import re

watson = re.sub(r';', r',', watson)  #replace the semicolon with colon
watson = watson.strip().split('|')
removeWatson = list(watson)

for i in range(len(watson)):

    for j in range(len(watson)):

        if j == i:
            continue

        if " ".join(watson[i].strip().lower().split()) in " ".join(watson[j].strip().lower().split()):
            removeWatson[i] = ''

print "|".join(filter(None, removeWatson))


#
# newString = []
#
# for line in string.lower().split('|'):
#
#     newString.append(" ".join(line.strip().split()))
#
# removeString = list(newString)
#
#











