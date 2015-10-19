# import re
#
# def answer(chunk, word):
#
#     final_string = []
#
#     for j in range(len(word)-1):
#
#         final_word = chunk[j:].split(word)
#
#         output = chunk[:j] + "".join(final_word)
#
#         final_string.append(str(output))
#         # word_position = [m.start() for m in re.finditer(word, chunk[:])]
#         #
#         # for i in range(len(word_position)):
#         #
#         #     if i == chunkLength-1:
#         #
#         #         final_word += chunk[word_position[i]+length:]
#         #
#         #     else:
#         #
#         #         final_word += chunk[word_position[i]+length:word_position[i+1]]
#
#     if len(final_string) >= 1:
#
#         return sorted(final_string)[0]
#     else:
#         return None
#
#
#
#
#
#
# #
# # There is no simple built-in string function that does what you're looking for, but you could use the more powerful regular expressions:
# #
# # >>> [m.start() for m in re.finditer('test', 'test test test test')]
# # [0, 5, 10, 15]
# #
# # If you want to find overlapping matches, lookahead will do that:
# #
# # >>> [m.start() for m in re.finditer('(?=tt)', 'ttt')]
# # [0, 1]
# #
# # If you want a reverse find-all without overlaps, you can combine positive and negative lookahead into an expression like this:
# #
# # >>> search = 'tt'
# # >>> [m.start() for m in re.finditer('(?=%s)(?!.{1,%d}%s)' % (search, len(search)-1, search), 'ttt')]
# # [1]