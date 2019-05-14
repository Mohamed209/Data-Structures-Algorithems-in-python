from UtilClasses.Node import Node
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
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        self.items.pop()
# Linked List implementation
class LinkedList:

    """singly-linked list in Python"""
    def __init__(self):
        self.head=None

    def isEmpty(self):
        return self.head==None

    def prepend(self,item):
        n=Node(item)
        n.setNext(self.head)
        self.head=n

    def append(self,item):
        if self.isEmpty():
            self.head=Node(item)
            return
        # traverse the list to find the last element
        current=self.head
        while current.getNext():
            current=current.getNext()
        current.setNext(Node(item))
        return
    def showItems(self):
        items=[]
        if self.isEmpty():
            return ("empty linked list")
        # traverse the list
        current=self.head
        items.append(current.getData())
        while current.getNext():
            current=current.getNext()
            items.append(current.getData())
        print(items)

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
    # remove by value and by index , insert at position
    def insert(self,item,position):

        n=Node(item)
        current = self.head
        for i in range(position-1):
            current=current.getNext()
        n.setNext(current.getNext())
        current.setNext(n.getData())

    def removeByIndex(self,position):

        current=self.head
        for i in range(position-1):
            current=current.getNext()
        newnext=current.getNext()
        newnext.setNext(newnext.getNext())
        current.setNext(newnext.getNext())