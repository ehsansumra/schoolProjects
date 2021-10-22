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

def reverseSentence(words: str):
    wordStack = Stack()
    wordList = words.split()

    for word in wordList:
        wordStack.push(word)
    
    reverseWordList = []
    while not wordStack.isEmpty():
        reverseWordList.append(wordStack.pop())
    
    return " ".join(reverseWordList)

def decimal2Binary(number):
    binStack = Stack()

    while not number == 0:
        remainder = number % 2
        number = number // 2
        binStack.push(str(remainder))
    
    binaryStr = ""
    while not binStack.isEmpty():
        binaryStr += binStack.pop()
    
    return binaryStr

def main():
    words = "stacks are very fun"
    print("Input:", words)

    reverseWords = reverseSentence(words)
    print("Output:", reverseWords)

if __name__ == "__main__":
    print(decimal2Binary())
