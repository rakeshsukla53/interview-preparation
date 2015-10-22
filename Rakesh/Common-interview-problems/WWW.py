__author__ = 'rakesh'

def answer(sentence):
    '''
    :param sentence: List of sentences
    :return: remove extra sentences
    output: Watson represents a first step into cognitive systems, a new era of computing.|what does watson represent
    '''

    words = sentence.split("|")
    finalAnswer = sentence.split("|")

    for i in range(len(words)):

        for j in range(len(words)):

            if i == j:
                continue

            if " ".join(words[i].strip().split()).lower().replace(";", ",") in " ".join(words[j].strip().split()).lower().replace(";",","):
                try:
                    finalAnswer.remove(words[i])
                except ValueError:
                    pass
    print "|" .join(finalAnswer)

answer('watson  Represents|watson represents|Watson represents a first step into cognitive systems, a new era of computing.|first step into  Cognitive|Cognitive Systems; a new era|what does watson represent')

