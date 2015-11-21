
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        def answer(root):
            if root == None:
                return 0
            else:
                left = answer(root.left)
                if left is False:
                    return False
                right = answer(root.right)
                if right is False:
                    return False
                value = 1 + max(left, right)
                difference = abs(left - right)
                if difference > 1:
                    return False
                return value
        result = answer(root)
        if result:
            return True
        return result

# checkout visualization http://www.pythontutor.com/visualize.html#code=class+BinarySearchTree%3A+++%23now+you+can+perform+any+type+of+opertion+on+this+tree%0A%0A++++def+__init__(self,+value%29%3A%0A%0A++++++++self.value+%3D+value%0A++++++++self.right+%3D+None%0A++++++++self.left+%3D++None%0A%0A++++def+insert(self,+data%29%3A++%23this+will+take+the+value+and+insert+accordingly%0A%0A++++++++if+data+%3E+self.value%3A%0A++++++++++++if+self.right+%3D%3D+None%3A%0A++++++++++++++++self.right+%3D+BinarySearchTree(data%29%0A++++++++++++else%3A%0A++++++++++++++++self.right.insert(data%29%0A%0A++++++++elif+data+%3C+self.value%3A%0A++++++++++++if+self.left+%3D%3D+None%3A%0A++++++++++++++++self.left+%3D+BinarySearchTree(data%29%0A++++++++++++else%3A%0A++++++++++++++++self.left.insert(data%29%0A++++++++else%3A%0A++++++++++++self.data+%3D+data%0A++++++++++++%0Adef+isBalanced(root%29%3A%0A++++++++%22%22%22%0A++++++++%3Atype+root%3A+TreeNode%0A++++++++%3Artype%3A+bool%0A++++++++%22%22%22%0A++++++++if+root+is+None%3A%0A++++++++++++return+True%0A++++++++++++%0A++++++++def+answer(root%29%3A%0A++++++++++++%0A++++++++++++if+root+%3D%3D+None%3A%0A++++++++++++++++return+0%0A++++++++++++else%3A%0A++++++++++++++++left+%3D+answer(root.left%29%0A++++++++++++++++if+left+is+False%3A%0A++++++++++++++++++++return+False+%0A++++++++++++++++right+%3D+answer(root.right%29%0A++++++++++++++++if+right+is+False%3A%0A++++++++++++++++++++return+False%0A++++++++++++++++value+%3D+1+%2B+max(left,+right%29%0A++++++++++++++++difference+%3D+abs(left+-+right%29%0A++++++++++++++++if+difference+%3E+1%3A%0A++++++++++++++++++++return+False%0A++++++++++++++++return+value%0A++++++++++++%0A++++++++result+%3D+answer(root%29%0A++++++++if+result%3A%0A++++++++++++return+True%0A++++++++return+result%0A%0A%0Aroot+%3D+BinarySearchTree(10%29%0Aroot.insert(8%29%0Aroot.insert(7%29%0Aroot.insert(6%29%0Aroot.insert(11%29%0A%0AisBalanced(root%29&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&textReferences=false&py=2&rawInputLstJSON=%5B%5D&curInstr=135
