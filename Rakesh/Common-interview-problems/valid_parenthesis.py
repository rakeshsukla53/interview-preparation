

def valid(values):

    stack = []
    dict = {"]":"[", "}":"{", ")":"("}
    for char in values:
        if char in dict.values():
            stack.append(char)
        elif char in dict.keys():
            if stack == [] or dict[char] != stack.pop():
                return 'NO'
        else:
            return 'NO'
    if stack == []:
        return 'YES'
    else:
        return 'NO'

def Braces(values):

    result = []

    for i in values:
        result.append(valid(i))

    return result





