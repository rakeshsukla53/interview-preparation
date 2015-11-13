import string
a_to_z = string.lowercase
a_to_m = string.lowercase[0:13]

import string

def is_pangram(phrase):
    print phrase.lower()
    print set('rakesh')
    print set((phrase.lower()))
    print set(string.lowercase)
    print set(string.lowercase).issubset(set(phrase.lower()))

is_pangram('The quick brown fox jumps over the lazy dog') # True
is_pangram('The quick brown fox jumps over he lazy dog') # False


