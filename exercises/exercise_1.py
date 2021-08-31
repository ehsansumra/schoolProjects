# Ehsan Sumra
# CSC 212

# solution 1
def useRecursion(strInput: str, wordMap: dict):
    if len(strInput) == 0:
        return
    spaces = 0
    for letter in strInput:
        if letter == " ": # if a space is reached
            spaces += 1
            
            strIndex = strInput.index(letter)
            word = strInput[:strIndex] # Slicing the string before the space
            updateWordCount(word, wordMap) # update this word to the dictionary
            
            skip = strIndex + 1
            newStr = strInput[skip:] # create a new string
            useRecursion(newStr, wordMap) # recursion
            
            return 
    if spaces == 0:
        updateWordCount(strInput, wordMap)

# solution 2: using split
def easyParse(strInput: str, wordMap: dict):
    stringList = strInput.split() # string to array with words as elements
    for word in stringList:
        updateWordCount(word, wordMap)
    return 

def updateWordCount(word: str, wordMap: dict):
    if word in wordMap:
        wordMap[word] += 1
    else:
        wordMap[word] = 1

def printMap(wordMap: dict):
    for key in wordMap:
        if key != "":
            print(key, wordMap[key])

def MethodOne():
    wordMap = {}
    strInput = input("Enter a string: ")
    useRecursion(strInput, wordMap)
    printMap(wordMap)

def MethodTwo():
    wordMap = {}
    strInput = input("Enter a string: ")
    easyParse(strInput, wordMap)
    printMap(wordMap)

if __name__ == "__main__":
    MethodTwo()
    
