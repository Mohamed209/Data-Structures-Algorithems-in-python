from LinearDs.LinearDs import Stack
# function to convert number to any base
def toBase(number,base):
    s=Stack()
    conversion=''
    if number<=0:return 0
    else :
        while number!=0:
            s.push(str(number%base))
            number//=base
        while not s.isEmpty():
            conversion+=s.top()
            s.pop()
        return  conversion
print(toBase(8,2))