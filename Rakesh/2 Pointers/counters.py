
from collections import Counter
from string import punctuation
from string import translate
import re

word = ['p', 'e', 'r', 'f', 'e', 'c', 't', '  ', 'm', 'a', 'k', 'e', 's', '  ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e']

print [letter for word in "".join(word).split()[::-1] for letter in word]

text = "practice makes perfect get perfect by practice just practice"

print translate(text, punctuation)

s = re.sub(r'[^\w\s]+', '', text)

print s

def word_count(text):
   return Counter(re.sub(r'[^A-Za-z ]+', '', text).split(' '))

   Counter(re.sub(r'[^\w\s]', '', text).split(' '))
   myString.translate(None, string.punctuation)


