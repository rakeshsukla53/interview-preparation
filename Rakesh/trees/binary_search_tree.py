__author__ = 'rakesh'

#create a binary tree

class BinaryTree:

    def __init__(self, value):
        self.value = value
        self.rightChild = None
        self.leftChild = None

    def insertLeft(self, value):
        if self.leftChild == None:
            self.leftChild = BinaryTree(value)  #assuming the value you want to enter is 10
        else:
            t = BinaryTree(value)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, value):
        if self.rightChild == None:
            self.rightChild = BinaryTree(value)
        else:
            t = BinaryTree(value)
            t.rightChild = self.rightChild
            self.rightChild = t

    def isLeaf(self):
        return (self.leftChild == None) and (self.rightChild == None)


    def getLeftChildValue(self):
        return self.leftChild.getRootValue()

    def getRightChildValue(self):
        return self.rightChild.getRootValue()

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def getRootValue(self):
        return self.value

    def setRootValue(self, obj):
        self.value = obj

    def inOrder(self):   #basically inOrder goes from left center right
        if self.leftChild:
            self.leftChild.inOrder()
        print self.value
        if self.rightChild:
            self.rightChild.inOrder()

    def postOrder(self):
        if self.leftChild:
            self.leftChild.postOrder()
        if self.rightChild:
            self.rightChild.postOrder()
        print self.value

    def endLeftChild(self):  #Go the extreme left value
        while self.leftChild != None:
            #print self.getRootValue()  #You can check the left values as we go by
            self = self.getLeftChild()
        return self

    def endRightChild(self):   #Go to the extreme right value
        while self.RightChild != None:
            #print self.getRootValue()  #You can check the right values
            self = self.getRightChild()
        return self

    def preOrder(self):
        print self.value
        if self.leftChild:
            self.leftChild.preOrder()
        if self.rightChild:
            self.rightChild.preOrder()

def height(tree):   #you can print out the height of the tree
    if tree == None:
        return -1
    else:
        return 1 + max(height(tree.leftChild), height(tree.rightChild))

k = BinaryTree(10)
k.insertLeft(20)
#k.insertLeft(5)
#k.insertLeft(4)
#k.insertLeft(3)
#k.insertLeft(2)
k.insertRight(30)
#k.endLeftChild().insertLeft(30)  #you can go the extreme of the left child and insert some values there
#print k.getRootValue()   #K is always the top of the root and it is always pointing to the top value
k.inOrder()  #use this http://www.codeskulptor.org/viz/index.html for checking the visualization of it

#you can create whatever type of tree you want to create here
#print height(k)








