__author__ = 'rakesh'

from collections import defaultdict

def bigram(sentence):
    '''
    :param List of sentences
    :return: Datastructure containing sentence and bigram

    Datastructure 1 - {'the peck': 1, 'Peter Piper': 4, 'peppers Peter': 2, 'A peck': 1, 'Piper picked': 3, 'peck of': 4, 'peppers  where': 1, 'Piper picked.': 1, 'pickled peppers': 2, 'of pickled': 4, 'pickled peppers ': 1, 'a peck': 2, 'where the': 1, 'picked If': 1, 'picked a': 2, 'If Peter': 1, 'pickled peppers.': 1, 'peppers A': 1}

    Datastructure 2 - {"Peter Piper picked a peck of pickled peppers. A peck of pickled peppers Peter Piper picked. If Peter Piper picked a peck of pickled peppers, where's the peck of pickled peppers Peter Piper picked?": ['the peck', 'Peter Piper', 'peppers Peter', 'A peck', 'Piper picked', 'peck of', 'peppers  where', 'Piper picked.', 'pickled peppers', 'of pickled', 'pickled peppers ', 'a peck', 'where the', 'picked If', 'picked a', 'If Peter', 'pickled peppers.', 'peppers A']}
    '''
    allWords = sentence.split(" ")      #Split the whole sentence into words
    dataFrequency = defaultdict(int)    #Hashmap defined
    sentenceBigram = dict()             #This is the second datastructure for storing sentence and list of bigrams
    for i in range(len(allWords) - 1):

        pair = allWords[i].split(".")[0].split("'")[0] + " " + allWords[i + 1].split("?")[0].split("'")[0]
        wordPair = " ".join(pair.split(","))
        dataFrequency[wordPair] += 1

    sentenceBigram[sentence] = dataFrequency.keys() #Second DataStructure containing sentence and list of bigrams

bigram("Peter Piper picked a peck of pickled peppers. A peck of pickled peppers Peter Piper picked. If Peter Piper picked a peck of pickled peppers, where's the peck of pickled peppers Peter Piper picked?")

