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
# test class definition
s= Stack()
s.push(-100)
s.push(100)
print(s.showStack(),s.isEmpty(),s.size())
s.pop()
print(s.showStack(),s.isEmpty(),s.size(),s.top())
s.pop()
print(s.size())
s.pop()
# reverse a string using stack data structure
def reverse(string):
    stack=Stack() # create empty stack object
    srev='' # reversed string
    for character in string:
        stack.push(character)
    while not stack.isEmpty():
        srev+=stack.top()
        stack.pop()
    return srev
print(reverse('hello'))

# check for balanced Parentheses using stack
def isBalanced(exp):
    if len(exp)%2!=0 or len(exp)==0:
        return False
    else:
        s=Stack()
        for ch in exp:
            if ch in '(':
                s.push(ch)
            elif ch in ')':
                if s.isEmpty():return False
                else :s.pop()
        return s.isEmpty()
print(isBalanced('))(('))