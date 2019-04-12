'''def  angaramCheck(s1,s2):
    # sum all characters for both strings
    numrep = [sum([ord(n)for n in s1]), sum([ord(n)for n in s2])]
    return numrep[0]==numrep[1]
print(angaramCheck('listen','silent'))
print(angaramCheck('heart','earth'))'''
from LinearDs.LinearDs import *
ls=LinkedList()
ls.prepend(6)
ls.prepend(7)
ls.prepend('a')
ls.prepend('b')
ls.showItems()
ls.removeByIndex(2)
ls.showItems()