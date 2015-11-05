import urllib2
import re
from collections import defaultdict

def find_word_frequency():
    '''
    Count the number of times a word occurs in a file
    How to run:
    - Go to your terminal, then type python <name of the file>
    '''
    data = urllib2.urlopen('http://www.gutenberg.org/cache/epub/11/pg11.txt')
    # pattern to capture only words
    pattern = re.compile("[a-zA-Z][a-zA-Z0-9]*")
    word_count = defaultdict(int)
    count = False
    for line in data:
        if '*** START' in line:
            count = True
            # taking only those lines between start and end of project
            continue
        if 'End of Project Gutenberg' in line:
            break

        if count:
            for word in pattern.findall(line):
                word_count[word] += 1

    word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    return word_count

if __name__ == '__main__':

    word_frequency = find_word_frequency()
    for i in range(20):
        print word_frequency[i][0], word_frequency[i][1]


