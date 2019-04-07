from LinearDs.LinearDs import Stack
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