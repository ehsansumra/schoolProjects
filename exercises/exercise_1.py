
def testParse(strInput: str, map: dict):
    if len(strInput) == 0:
        return
    
    spaces = 0
    for letter in strInput:
        if letter == " ":
            spaces += 1
            
            strIndex = strInput.index(letter)
            word = strInput[:strIndex]
            updateWordCount(word, wordMap)
            
            skip = strIndex + 1
            newStr = strInput[skip:]
            testParse(newStr, wordMap)
            
            break
    
    if spaces == 0:
        updateWordCount(strInput, wordMap)  

def updateWordCount(word: str, wordMap: dict):
    if word in wordMap:
        wordMap[word] += 1
    else:
        wordMap[word] = 1

def printMap(wordMap: dict):
    for key in wordMap:
        if key != "":
            print(key, wordMap[key])


if __name__ == "__main__":
    wordMap = {}
    strInput = input("Enter a string: ")
    testParse(strInput, wordMap)
    printMap(wordMap)