
from collections import Counter

def isPangram(strings):

    letters = "abcdefghijklmnopqrstuvwxyz"
    output = []
    count = True

    for line in strings:

        word_frequency = Counter(line)
        del word_frequency[' ']
        print "".join(word_frequency)
        for w in letters:
            if w not in "".join(word_frequency):
               output.append('0')
               count = False
               break

        if count:
            output.append('1')

    return "".join(output)    


isPangram(['The quick brown fox jumps over the lazy dog'])

