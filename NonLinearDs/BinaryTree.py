# implementing tree data structure
class BinaryTree:
    def __init__(self, data):
        self.data = data
        # left and right are tree nodes
        self.rightchild = None
        self.leftchild = None

    def insertleft(self, newnode):
        self.leftchild = BinaryTree(newnode)

    def insertright(self, newnode):
        self.rightchild = BinaryTree(newnode)

    def getRightChild(self):
        return self.rightchild

    def getLeftChild(self):
        return self.leftchild

    def setRootVal(self, data):
        self.data = data

    def getRootVal(self):
        return self.data
r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertleft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertright('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())