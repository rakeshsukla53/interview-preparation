__author__ = 'rakesh'

#find the second largest element
#handiling duplicate keys in binary search tree

A = [20, 30, 40, 50, 60, 70, 30, 20, 11, 15, 16, 19, 23]

sLargest = []

class SecondLargest:

    def __init__(self, value):

        self.left = None
        self.right = None
        self.value = value

    def insert(self, data):  #this will take the value and insert accordingly

        if data > self.value:
            if self.right == None:
                self.right = SecondLargest(data)
            else:
                self.right.insert(data)

        elif data <= self.value:
            if self.left == None:
                self.left = SecondLargest(data)
            else:
                self.left.insert(data)
        else:
            self.data = data

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def getRootValue(self):
        return self.value

    def isleaf(self):
        return (self.right == None) and (self.left == None)

    def getleftValue(self):
        return self.left.getRootValue()

    def getrightValue(self):
        return self.right.getRootValue()

    def getleft(self):
        return self.left

    def secondLargest(self):   #finding the using modified inorder traversal to check the second largest element
        '''
        modified inorder traversal for producing the decreasing order list and then finding the second largest
        in all such questions recursion is neccessary and should be used
        '''
        if self.right:
            self.right.secondLargest()
        sLargest.append(self.value)
        if len(sLargest) == 2:
            print sLargest[-1]
            exit()
        if self.left:
            self.left.secondLargest()

    def inOrder(self):   #basically inOrder goes from left center right
        if self.left:
            self.left.inOrder()
        print self.value
        if self.right:
            self.right.inOrder()

    def postOrder(self):
        if self.left:
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        print self.value

    def preOrder(self):
        print self.value
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()

    def lookup(self, data, parent=None):
        '''
        Searching a particular value in the binary tree and then returning its parent and node
        This example also shows how to store the node and parent in recursion
        '''
        if data > self.value:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)

        elif data < self.value:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)   #refer to this note to under
            # http://www.pythontutor.com/visualize.html#mode=display
            #you need to return the value because everything is recursive here

        else:
            print "Node is %s" % self.getRootValue()
            print "Parent is %s" % parent.getRootValue()

            return self, parent

    def delete(self, data):

        node, parent = self.lookup(data)

        if node is not None:
            children_count = node.children_count()

        if children_count == 0:
            if parent:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None

                del node

            else:
                self.data = 0

        elif children_count == 1:
            #if there is only one node then you need to replace it with its child
            if node.left:
                n = node.left
            if node.right:
                n = node.right

            if parent:
                if parent.left is node:
                    parent.left = n
                else:
                    parent.right = n
                del node

        else:
            parent = node
            successor = node.right
            while successor.left:
                parent = successor
                successor = successor.left

            node.value = successor.value  #find the inorder successor of the node and replace it
            if parent.left == successor:
                parent.left = successor.right

            else:
                parent.right = successor.right

    def reverse(self):
        '''
        reversing the left and right values of the array
        reversing the binary search tree or binary tree. Simply changing the links
        '''
        self.left, self.right = self.right, self.left
        if self.left != None:
            self.left.reverse()
        if self.right != None:
            self.right.reverse()

        return self

    def compare_two_tree(self, node):  #when you are comparing two trees then its right and left child should be equal

        if node is None:
           print "Tree are not equal"
           return False


        if self.value != node.value:
            print "Trees are not equal"
            return False

        else:
            if self.left:
                self.left.compare_two_tree(node.left)
            print self.value
            if self.right:
                self.right.compare_two_tree(node.right)  #if it printouts all the trees values then they are equal
        #just use simply use the inorder traversal and compare each value as we go along

    def children_count(self):

        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count

def height(tree):   #you can print out the height of the tree
    if tree == None:
        return 0
    else:

        return 1 + max(height(tree.left), height(tree.right))

root = SecondLargest(20)

for i in A[1:]:

    root.insert(i)

#root.secondLargest()

# root.reverse() #reversing the binary search tree or binary stree
# root.inOrder() #Now we don't have to use the modified inOrder equation
# root.reverse()
# root.inOrder()

print height(root)

