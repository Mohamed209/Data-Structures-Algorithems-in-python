from LinearDs.LinearDs import Dequeu
def palindromeCheck(string):
    d=Dequeu()
    for char in string:
        d.addFront(char)
    flag=True
    while d.size()>1 and flag:
        if (d.removeFront()!=d.removeRear()):
            flag=False
    return flag
print(palindromeCheck("lsdkjfskf"))
print(palindromeCheck("radar"))