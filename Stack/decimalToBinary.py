from Stack import Stack
def decimalToBinary(decimal):
    s=Stack()
    binary=''
    while decimal !=0:
        s.push(str(decimal%2))
        decimal//=2
    while not s.isEmpty():
        binary+=s.top()
        s.pop()
    return  binary
print(decimalToBinary(12549744))