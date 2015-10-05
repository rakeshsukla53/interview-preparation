__author__ = 'rakesh'

class Reverse:

    def __init__(self, data):
        self.data = data
        self.index = len(str(data))

    def __iter__(self):
        return self

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

def main():
    rev = Reverse('1234')
    for cha in rev:
        print cha

if __name__ == '__main__':
    main()

#So here the __iter_ funtion will be automatically called
#So when you create a object rev , it automatically stores all the function which is possible on it
#if you use an int object then it doesn't have any attribute ans __getitem but this class which is defined for int
#does contain it
