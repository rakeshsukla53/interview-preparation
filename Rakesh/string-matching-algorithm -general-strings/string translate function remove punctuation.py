from string import punctuation
import string

text = "practice() makes; perfect, get""# perfect by practice just practice"
table = string.maketrans('a', 'a')
# print table, len(table)

# remove all punctuation using translate
print text.translate(table, str(punctuation))
