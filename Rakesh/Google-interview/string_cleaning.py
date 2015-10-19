
def answer(chunk, word):

    shortestWord = []

    shortestWord.append("".join(chunk.split(word)))

    shortestWord.append("".join(chunk.rsplit(word)))

    if len(shortestWord) >= 1:

        return sorted(shortestWord)[0]

    else:
        return None

print answer("lolololo", "lo")

