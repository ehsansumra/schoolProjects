# Ehsan Sumra
# Assignment 5

import random

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

# -- Part 1 --

# Reverse a string by pushing its characters to a stack, and then create a new string by popping from that stack.
def reverseString(string):
    testStack = Stack()

    for letter in string:
        testStack.push(letter)
    
    word =''
    while not testStack.isEmpty():
        letter = testStack.pop()
        word += letter

    return word

# Tests a string if it is a palindrome by reversing it using a stack
# Then checks if the word and reversed word are equal
def isPalindrome(word: str) -> bool:
    reverse = reverseString(word)
    return word == reverse

# Tests a list of strings: print True if palindrome, False if not.
def listPalindromeTester(wordList: list):
    print("\n--- Testing Palindrome ---")
    for word in wordList:
        boolean = isPalindrome(word)
        print(word, boolean)

# General test function
def testPalindromes():
    palindromes = ["noon", "civic", "radar", "level", "rotor", "reviver", "racecar", "redder", "madam", "refer"]
    nonPalindromes = ["noo", "civi", "adar", "evel", "roto", "eviver", "raceca", "redde", "adam", "refe"]
    listPalindromeTester(palindromes)
    listPalindromeTester(nonPalindromes)

# -- Part 2 --

# Generate a list of random values from 1 to 200, for the purpose of testing.
def generateValues():
    genList = []
    for i in range(20):
        genList.append(random.randint(1,200))
    return genList 

# Takes a stack, pops each value, pushes them into a temporary stack. 
# It will find the maximum value in this iteration,
# Then pop everything from the temp stack and push it back into the original stack
# This will return the original stack to all of its values in the correct order.
def maxStack(stack: Stack) -> bool:
    tempStack = Stack()
    maxNum = 0

    while not stack.isEmpty():
        current = stack.pop()
        tempStack.push(current)
        if current > maxNum:
            maxNum = current

    while not tempStack.isEmpty():
        stack.push(tempStack.pop())
    
    return maxNum

# Simply display all items in stack, returning the original stack in correct order.
def printStack(stack: Stack):
    print("--- Printing Stack ---")
    tempStack = Stack()

    while not stack.isEmpty():
        current = stack.pop()
        tempStack.push(current)
        print(current)

    while not tempStack.isEmpty():
        stack.push(tempStack.pop())

# Test function that displays the stack before and after the maxStack() operation,
# to show that the stack has the same values in the correct order.
def testMaxStack():
    stack = Stack()
    testList = generateValues() 
    for value in testList:
        stack.push(value)

    print("\nBefore Stack iteration")
    printStack(stack)

    max = maxStack(stack)
    print("\nMax Value: ", max)

    print("\nAfter Stack iteration")
    # Showing that the stack values are the same before and after.
    printStack(stack)

def main():
    # End the program whenever you want!
    while True:
        option = int(input("Enter 1 for part 1 (palindromes), 2 for part 2 (max value in stack), 3 for a general test, 0 to end the program. "))
        
        if option == 1:
            word = input("Enter a string: ")
            palindromeBoolean = isPalindrome(word)
            print(f"Is {word} a palindrome? {palindromeBoolean}")
        
        elif option == 2:
            testMaxStack()
        
        elif option == 3:
            testPalindromes()
            testMaxStack()

        elif not option:
            break
        else:
            print("Invalid input")
            
if __name__ == "__main__":
    main()
    
    
