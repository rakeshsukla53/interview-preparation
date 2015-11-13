def string_map(f): #accepts a function on strings, splits the string, maps the function, then rejoins
    def __f(s, *args, **kwargs):
       return " ".join(f(t, *args, **kwargs) for t in s.split())
    return __f

@string_map
def reverse_string(s):
    return s[::-1]

print reverse_string('my life is beautiful')

