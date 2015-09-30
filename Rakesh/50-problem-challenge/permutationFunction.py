__author__ = 'rakesh'

result = list()

def generate(string, start, end):
    current = 0
    if start == end - 1:
        if not string in result:
            result.append(string)
    else:
        for current in range(start, end):
            x = list(string)
            x[start], x[current] = x[current], x[start]
            generate("".join(x), start + 1, end)

def main():
    string = 'ABC'
    length = len(string)
    generate(string, 0, length)
    print result

if __name__ == '__main__':
    main()
