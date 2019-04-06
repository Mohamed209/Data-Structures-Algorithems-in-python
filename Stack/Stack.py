# implement a class to simulate a stack data structure
class Stack:
    def __init__(self):  # init function should create an empty list
        self.items=[]
    def showStack(self):
        return self.items
    def isEmpty(self):  # check if stack has elements or not
        return self.items==[]
    def size(self):  # get stack size
        return len(self.items)
    def push(self,item): # push element to the stack
        self.items.append(item)
    def pop(self): # remove stack top item
        try:self.items.pop()
        except IndexError:print("you can not pop from empty stack")
    def top(self):
        return self.items[-1]