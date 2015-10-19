__author__ = 'rakesh'

def answer(document, searchTerms):

    loopSearchTerms = []

    for j in searchTerms:
        loopSearchTerms.append(j)

    stringList = document.split(" ")

    start, end = 0, 0

    shortSnippet = []

    count = 1

    d = dict()

    for j in range(len(searchTerms)):

        for i in range(len(stringList)):

            if searchTerms[j] == stringList[i]:

                d.setdefault(searchTerms[j], []).append(i)

    itemPosition = sorted(sum(d.values(), []))

    for k in itemPosition:

        start = k

        for i in range(k, len(stringList)):

            if stringList[i] in loopSearchTerms:

                loopSearchTerms.remove(stringList[i])

                end = i

                if len(loopSearchTerms) == 0:

                    if count == 1:

                        shortSnippet.append(stringList[start:end+1])
                        count += 1

                    if len(stringList[start:end+1]) < len(shortSnippet[0]):
                        shortSnippet = []
                        shortSnippet.append(stringList[start:end+1])

                    for j in searchTerms:
                        loopSearchTerms.append(j)

                    break

    try:

        return " ".join(shortSnippet[0])

    except IndexError:
        pass

print answer("However a division bench allowed the revenue department's appeal and said while interpreting provisions relating to classification of commodities, the predominant test to be applied was based on the understanding of the commodity in its popular and commercial sense", ["revenue", "classification", "However"])

