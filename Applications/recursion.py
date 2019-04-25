def listSum (list):
    # base case
    if len(list)==1:
        return list[0]
    else :
        return list[0]+listSum(list[1:]) # moving toward the base case
def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)
def toStr(n,base):

    convertString = "0123456789ABCDEF"
    if n<base:
        return convertString[n]
    else :
        return toStr(n//base,base)+convertString[n%base]

def reverseString(string):
    if len(string)==1:
        return string
    else :
        return string[-1]+reverseString(string[:len(string)-1])

print(listSum([1,3,5,7,9]))
print(fact(8))
print(toStr(1453,16))
print(reverseString('hello'))
print(reverseString('follow'))