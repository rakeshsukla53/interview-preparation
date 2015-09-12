__author__ = 'rakesh'

#https://www.hackerrank.com/challenges/word-order

#Idea - Simply use collection counters and then derive its keys

from collections import Counter

words = []
frequencyList = []

N = input()
for i in range(N):

    words.append(raw_input().strip())

wordFrequency = Counter(words)

for i in words:

    frequencyList.append(words.index(i))

print len(set(wordFrequency.keys()))

print " ".join(map(str, [wordFrequency[words[i]] for i in list(set(frequencyList))]))


