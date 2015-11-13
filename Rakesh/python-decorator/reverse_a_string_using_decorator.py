
# s = 'my life is beautiful'
#
# def reverse_sentence(s):
#
#     string_reverse = []
#
#     for i in s.split():
#         string_reverse.append("".join(list((reversed(i)))))
#
#     print " ".join(string_reverse)
#
# reverse_sentence(s)

def reverse_sentence(fn):  # a decorator accepts a function as its argument
    def __inner(s, *args, **kwargs):  # it will return this modified function
       string_reverse = []
       for i in s.split():
           string_reverse.append("".join(list((reversed(i)))))
       return fn(" ".join(string_reverse), *args, **kwargs)
    return __inner  # return the modified function which does your string reverse on i

@reverse_sentence
def printer(s):
    print(s)

printer("hello world")



