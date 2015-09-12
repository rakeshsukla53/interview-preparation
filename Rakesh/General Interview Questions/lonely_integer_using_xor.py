__author__ = 'rakesh'

def lonelyinteger(a):
    k = a[0]
    for i in range(1, len(a)):
        k = k ^ a[i]
    return k
if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)


#this is another way to solve the whole problem

