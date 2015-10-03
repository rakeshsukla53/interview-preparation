__author__ = 'rakesh'


class BinarySearchTree:   #now you can perform any type of opertion on this tree

    def __init__(self, value):

        self.value = value
        self.right = None
        self.left =  None

    def insert(self, data):  #this will take the value and insert accordingly

        if data > self.value:
            if self.right == None:
                self.right = BinarySearchTree(data)
            else:
                self.right.insert(data)

        elif data < self.value:
            if self.left == None:
                self.left = BinarySearchTree(data)
            else:
                self.left.insert(data)
        else:
            self.data = data

    def isleaf(self):
        return (self.right == None) and (self.left == None)

    def getleftValue(self):
        return self.left.getRootValue()

    def getrightValue(self):
        return self.right.getRootValue()

    def getleft(self):
        return self.left

    def getright(self):
        return self.right

    def getRootValue(self):
        return self.value

    def setRootValue(self, obj):
        self.value = obj

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

    def printout(self):   #this is the inorder traversal of the whole tree. Inorder traversal will give you all whole tree

        if self.left:
            self.left.printout()
        print self.value
        if self.right:
            self.right.printout()

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

    def reverseTree(self):
        self.left, self.right = self.right, self.left
        if self.left != None:
            self.left.reverseTree()
        if self.right != None:
            self.right.reverseTree()

    def rootToLeaf(self, paths=[]):
        paths = paths + [str(self.value)]
        if self.left == None and self.right == None:
            return paths
        if self.left != None:
            newpath = self.left.rootToLeaf(paths)
            if newpath:
                print "->".join(newpath)
        if self.right != None:
            oldpath = self.right.rootToLeaf(paths)
            if oldpath:
                print "->".join(oldpath)

    def binaryRightSideView(self, paths=[]):
        paths = paths + [self.value]
        if self.left == None and self.right == None:
            return paths
        if self.right != None:
            newpath = self.right.binaryRightSideView(paths)
            if newpath:
                print newpath #Stand on the right side of the tree and then check

    def findParent(self, data, parent=None):
        if data > self.value:
            if self.right is None:
                return None, None
            return self.right.findParent(data, self)

        elif data < self.value:
            if self.left is None:
                return None, None
            return self.left.findParent(data, self)   #refer to this note to under
            # http://www.pythontutor.com/visualize.html#mode=display
            #you need to return the value because everything is recursive here

        else:
            return parent.getRootValue()

    def lowestCommonAncestor(self, p, q):
        '''
        find the lowest common ancestor of two nodes
        '''
        if (p > self.value and q < self.value) or (p < self.value and q > self.value):
            return self.value  #that will be the root
        if p > self.value and q > self.value:
            return self.right.lowestCommonAncestor(p, q)
        if p < self.value and q < self.value:
            return self.left.lowestCommonAncestor(p, q)
        if p == self.value and (q > self.value or q < self.value):
            return p
        if q == self.value and (p > self.value or p < self.value):
            return q

    def returnParent(self, data, parent=None):
        '''
        :return parent of the node and through parent we can findout which is right or left node
        '''
        if data > self.value:
            if self.right != None:
                return self.right.returnParent(data, self)
            else:
                return None
        if data < self.value:
            if self.left != None:
                return self.left.returnParent(data, self)
            else:
                return None
        if self.value == data:
            return parent

    def valueExist(self, data):
        '''
        Checking whether the value exist in the tree or not
        :return True or False (Whether the value exists or not
        '''
        if data > self.value:
            if self.right != None:
                return self.right.valueExist(data)
            else:
                return None
        if data < self.value:
            if self.left != None:
                return self.left.valueExist(data)
            else:
                return None
        if self.value == data:
            return self

    def inorderSuccessor(self, data):
        '''
        :return the inorder successor of the node
        '''
        presentValue = self.valueExist(data)
        if presentValue is not None:
            if presentValue.right == None:
                try:
                    while self.returnParent(presentValue.getRootValue()).left != presentValue:
                        presentValue = self.returnParent(presentValue.getRootValue())
                        if presentValue is None:
                            return None
                    return self.returnParent(presentValue.getRootValue())
                except AttributeError:
                    return None
            else:
                presentValue = presentValue.right
                while presentValue.left != None:
                    presentValue = presentValue.left
                return presentValue
        else:
            return None

    def invertBinaryTree(self):
        '''
        invert the binary tree and it is fairly very simple
        '''
        self.left, self.right = self.right, self.left
        if self.left != None:
            self.left.invertBinaryTree()
        if self.right != None:
            self.right.invertBinaryTree()

    def breadthForSearch(self):  #so the breadth for search if perfectly working
        from collections import deque
        '''
        for breadth for search you have the use the deque
        '''
        result = []
        d = deque()
        d.append(self)
        while len(d) != 0:
            if d[0].left != None:
                d.append(d[0].left)
            if d[0].right != None:
                d.append(d[0].right)
            result.append(d.popleft().value)

        return result





def height(tree):   #you can print out the  height of the tree
    if tree == None:
        return 0
    else:
        return 1 + max(height(tree.left), height(tree.right))

def isValidBST(root, validBinaryTree=[]):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return False

        if root.left != None:
            isValidBST(root.left, validBinaryTree)
        validBinaryTree.append(root.value)
        if root.right != None:
            isValidBST(root.right, validBinaryTree)

        for i in range(len(validBinaryTree)-1):
            if validBinaryTree[i] > validBinaryTree[i+1]:
                return False

        return True

root = BinarySearchTree(10)

root.insert(5)
root.insert(3)
root.insert(6)
root.insert(11)
root.upsideDownBinaryTree(root)
# root.insert(12)
# root.insert(14)
# print root.breadthForSearch()
#print isValidBST(root)
#root.preOrder()
# root.insert(20)
# root.insert(17)
# root.insert(16)
# root.insert(25)
# root.insert(27)
# root.insert(13)
# print root.inorderSuccessor(11).getRootValue()
# #root.delete(3)  # 1 is deleted from the binary tree
#root.compare_two_tree(node)
#Questions
#root.invertBinaryTree()
#print root.reverseTree()
#root.binaryRightSideView()
#print root.lowestCommonAncestor(4, 2)
#root.inOrder()
'''
p = height(root.left)

q = height(root.right)

print "Total diameter of the tree is %d" %(p + q + 1)   #diameter of the tree

#for finding diameter the length of right subtree and length of left subtree and add 1

#the height of tree is calculated recursively
'''















