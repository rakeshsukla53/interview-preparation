__author__ = 'rakesh'


from collections import Counter

words = []
frequencyList = []

N = input()
for i in range(N):

    words.append(raw_input().strip())

wordFrequency = Counter(words)

print len(wordFrequency.keys())

for word in words:
    point = wordFrequency.pop(word, None) #remove the key from the dictionary if the word is found. this a quite a way using pop
    #print point, wordFrequency
    if point == None:
        continue
    else:
        print point,  #this comma removes the newline character for printing. This is a very clever way of printing

