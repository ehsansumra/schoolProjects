# Ehsan Sumra
# Exercise 1

def storeWord(word: str):
    letterList = []
    for letter in word:
        letterList.append(letter)
    return letterList

def processMatch(string: str, matchIndex: int, letterList: list) -> bool:
    
    stringEnd = False
    for letterI in range(len(letterList)):       

        if (matchIndex == len(string)):
            stringEnd = True

        if not stringEnd and letterList[letterI] == string[matchIndex]:
            isMatch = True
        
        else: isMatch = False;       
        
        matchIndex += 1
    
    return isMatch

def processString(string: str, match: str) -> list:
    indexList = []
    letterList = storeWord(match)
    
    for index in range(len(string)):
        
        if letterList[0] == string[index]:
            
            if processMatch(string, index, letterList):
                indexList.append(index)
    
    return indexList

def printIndex(indexList: list):
    if len(indexList) == 0:
        print("Not found")
        return
    
    for index in indexList:
        print(index, end = " ")

def exerciseOne():
    print("\n", "- " * 30)
    inputString: str = input("\nEnter a string: ")
    inputMatch: str = input("\nEnter a word you want to find the index of: ")
    indexList = processString(inputString, inputMatch)
    printIndex(indexList)

# Exercise 2
def parseStrList(strList: str) -> list:
    parseBrackets = strList.replace("[", "")
    parseBrackets = parseBrackets.replace("]", "")
    parseSpaces = parseBrackets.replace(" ", "")
    numList = list(map(int, parseSpaces.split(",")))
    
    return numList

def sliceList(numList: list, indexOne: int, indexTwo: int) -> list:
    indexTwo += 1
    newList = numList[:indexOne] + numList[indexTwo:]
    return newList

def findAllIndexes(numList: list, num: int):
    iList = []
    for index in range(len(numList)):
        if num == numList[index]:
            iList.append(index)

    return iList

def filterList(numList: list):
    sixMatch = False
    sixIndex = None
 
    for index in range(len(numList)):
        if numList[index] == 6:
            if not sixMatch:
                sixIndex = index
            sixMatch = True
        
        if sixMatch and numList[index] == 7 and (sixIndex < index):
            newList = sliceList(numList, sixIndex, index)
            return newList

def check67(numList: list) -> bool:
    # check if there exists a 6 extending to a 7 in the list
    sixList = findAllIndexes(numList, 6)
    sevenList = findAllIndexes(numList, 7)

    if (not sixList) or (not sevenList):
        return False

    if sixList[0] < sevenList[-1]:
        return True
    else: 
        return False

def slice67(numList: list):
    
    if check67(numList): # base case - check if there exists a 6 extending to a 7 in the list
        newList = filterList(numList) # remove one instance of 6-7 from the list
        numList = slice67(newList) # recursion
    return numList

def sum67(numList: list):
    slicedList = slice67(numList) # removes all instances of 6->7 in the list
    sum = 0
    for num in slicedList:
        sum += num
    return sum

def exerciseTwo():
    strList = input("Enter a list of numbers: ")
    numList = parseStrList(strList)
    print(sum67(numList))


# Display

if __name__ == "__main__":
    while True:
        userInput = input("\nEnter 1 for Exercise 1, 2 for Exercise 2, 3 to end the program:\n")
        if userInput == "1":
            exerciseOne()

        elif userInput == "2":
            exerciseTwo()

        elif userInput == "3":
            break

        else:
            print("Input Error: Type just the number and press enter")

