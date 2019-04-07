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
            self.items.pop()
        except IndexError:
            print("you can not pop from empty stack")
    def top(self):
        return self.items[-1]
class Queue(LinearDs):
    """ to do write docstring"""