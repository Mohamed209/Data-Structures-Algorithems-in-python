from Stack import Stack
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