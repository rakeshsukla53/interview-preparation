__author__ = 'rakesh'

def reverse(data):

    for index in xrange(len(data)-1, -1, -1):
        yield data[index]

def main():
    rev = reverse('2324551234')
    for cha in rev:
        print cha

if __name__ == '__main__':
    main()

