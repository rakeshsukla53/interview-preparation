
dictionary = {'i': '', 'like': '', 'mangoes': '', 'mango': ''}

def word_split(s, words):
    d = [False] * len(s)
    for i in range(len(s)):
        for w in words:
            if w == s[i - len(w) + 1:i + 1] and (d[i - len(w)] or i - len(w) == -1):
                d[i] = True
    return d[-1]

print word_split('ilikemangoesmangomangoe', dictionary)

