# Ehsan Sumra
# Assignment 2

""" updates letterMap (dict) with a letter (str) entered in the parameter
    - for this dict,  {key = letter, value = number of occurrences}
    - creates a key for each letter entered
    - if the key exists, increment its value """
def updateLetterCount(letter: str, letterMap: dict):
    if letter in letterMap:
        letterMap[letter] += 1
    else:
        letterMap[letter] = 1

""" takes a string as parameter, return is a dictionary with this model:
    - {key = character of the string, value = number of occurrences within the string} """
def getCharacters(string: str) -> dict:
    letterMap = {}
    for letter in string:
        updateLetterCount(letter, letterMap)
    return letterMap

""" Comparing the two dictionaries (parameters) for each string (magazineStr and ransomeNoteStr).
    For each character in the ransomNote dict:
        if that character does not exist in the magazineStr dict in 
        greater-than-or-equal to amount to the ransomNote character,
        return False
        if it gets through the entire dictionary without a mismatch,
        return True """
def compareCharacters(magazineDict: dict, ransomNoteDict: dict) -> bool:
    for character in ransomNoteDict:
        if not ((character in magazineDict) and (magazineDict[character] >= ransomNoteDict[character])):
            print("mismatch: ", character)
            return False     
    return True

""" Takes two strings from the user. Turns each one into a dictionary
    The characters are then compared with compareCharacters()
    the boolean output of the function is printed """
def ransomNoteProblem():
    magazineDict = getCharacters(input("Enter a magazine string: "))
    ransomNoteDict = getCharacters(input("Enter a ransom note: "))
    print(compareCharacters(magazineDict, ransomNoteDict))

if __name__ == "__main__":
    ransomNoteProblem()

