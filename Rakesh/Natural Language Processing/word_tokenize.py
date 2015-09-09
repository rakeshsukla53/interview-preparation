__author__ = 'rakesh'
#http://pythonprogramming.net/tokenizing-words-sentences-nltk-tutorial/

from nltk.tokenize import sent_tokenize, word_tokenize

EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."

print(sent_tokenize(EXAMPLE_TEXT))

print(word_tokenize(EXAMPLE_TEXT))

'''
Now, looking at these tokenized words, we have to begin thinking about what our next step might be. We start to ponder about how might we derive meaning by looking at these words. We can clearly think of ways to put value to many words, but we also see a few words that are basically worthless. These are a form of "stop words," which we can also handle for.
'''

