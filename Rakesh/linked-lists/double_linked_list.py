
#Doubly linked list

class double:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def getData(self):
        return self.data

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def setData(self, newdata):
        self.data = newdata

class first:

    def __init__(self):
        self.head = None

    def add(self, data):
        if self.head == None:
            temp = double(data)
            self.head = temp
        else:
            temp = double(data)
            temp.right = self.head
            self.head.left = temp
            self.head = temp

    def circular(self):   #for making it a cicular linked list
        first = self.head
        while first.right != None:
            first = first.right

        first.right = self.head
        self.head.left = first

    def traverse(self):
        first = self.head
        while first != None:
            print first.getData()
            first = first.getRight()

mylist = first()

mylist.add(1)
mylist.add(2)
mylist.add(3)
mylist.add(4)
mylist.add(5)
mylist.add(6)
mylist.add(7)
mylist.add(8)
mylist.add(9)

mylist.traverse()
mylist.circular()







