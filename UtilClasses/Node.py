"""generic node class for linked list"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata
        return

    def setNext(self, newnext):
        self.next=newnext
        return