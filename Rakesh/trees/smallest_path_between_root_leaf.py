__author__ = 'rakesh'

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

def rootToLeaf(self, paths=[], minPath=[]):
        paths = paths + [str(self.value)]
        if self.left == None and self.right == None:
            return paths
        if self.left != None:
            newpath = self.left.rootToLeaf(paths, minPath)
            if newpath:
                minPath.append(len(newpath))
        if self.right != None:
            oldpath = self.right.rootToLeaf(paths, minPath)
            if oldpath:
                minPath.append(len(oldpath))


