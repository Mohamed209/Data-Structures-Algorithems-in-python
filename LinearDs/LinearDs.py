class LinearDs:
    """ to do add class doc string"""
    def __init__(self):
        """ initialize an empty python list"""
        self.items=[]
    def showItems(self):
        """ print the data structure contents """
        assert len(self.items)!=0 ,"data structure is empty"
        print(self.items)
        return
    def isEmpty(self):
        """ check if the data structure is empty or has elements"""
        return self.items==[]
    def size(self):
        """ return data structure size"""
        return len(self.items)
class Stack(LinearDs):
    """ to do write docstring """
    def push(self, item):  # push element to the stack
        self.items.append(item)
    def pop(self):  # remove stack top item
        try:
            return self.items.pop()
        except IndexError:
            print("you can not pop from empty stack")
    def top(self):
        return self.items[-1]
class Queue(LinearDs):
    """ to do write docstring"""
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
class Dequeu(LinearDs):
    """TO do write docstring"""
    def addFront(self,item):
        self.items.append(item)
    def addRear(self,item):
        self.items.insert(0,item)
    def removeFront(self):
        try:
            return self.items.pop()
        except IndexError:
            print("you can not remove from empty queue")
    def removeRear(self):
        try:
            return self.items.pop(0)
        except IndexError:
            print("you can not remove from empty queue")

