from structures import stack

letterStack = stack.Stack()

def reverseString(string):
    for letter in string:
        letterStack.push(letter)
    
    word =''
    while not letterStack.isEmpty():
        letter = letterStack.pop()
        word += letter

    return word

print(reverseString("hello world"))
        