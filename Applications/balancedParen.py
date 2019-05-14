from LinearDs.LinearDs import Stack
def match(ch):
    paren={
        ')':'(',
        '}':'{',
        ']':'['
    }
    return paren[ch]
# check for balanced Parentheses using stack
def isBalanced(exp):
    if len(exp)%2!=0 or len(exp)==0:
        return False
    else:
        s=Stack()
        for ch in exp:
            if ch in '([{':
                s.push(ch)
            elif ch in ')]}':
                if s.isEmpty():return False
                elif s.top()==match(ch):s.pop()
        return s.isEmpty()
print(isBalanced('{{([][])}()}'))
print(isBalanced('[{()]'))