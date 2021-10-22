# Ehsan Sumra
# Assignment 4
import time
import random

# Generate a unique list for testing worst case.
def generateUniqueList(n):
    orderedList = []
    for i in range(n):
        orderedList.append(i)
    return orderedList

# Generate a random list of ints with specified size and range of random values.
def generateList(n: int, start, stop):
    genList = []
    for i in range(n):
        genList.append(random.randint(start,stop))
    return genList 

# --- Algorithm 1 ---

# Update the dictionary (hashmap). Algorithm 2 has a better method for this.
def updateHashMap(dictionary: dict, item: float):
    if item in dictionary:
        dictionary[item] += 1
    else:
        dictionary[item] = 1

# Add all list items (keys) to a dictionary that records number of occurrences (values) for each item
def listToHashMap(newList: list):
    dictionary = {}
    for item in newList:
        updateHashMap(dictionary, item)
    return dictionary

# If the number of occurences (value) for any item (key) in the dictionary exceeds 1, return False (not unique)
def checkUnique(newList: list):
    dictionary = listToHashMap(newList)
    for item in dictionary:
        if dictionary[item] > 1:
            return False
    return True

# Algorithm One. T(n) = 1 + n(1 + 1 + 1) + 1 + n(1 + 1) + 1
    # T(n) = 3 + 5n
    # O(n)
def AlgorithmOne(testList):
    startTime = time.time()
    output = checkUnique(testList)
    endTime = time.time()
    executionTime = endTime - startTime
    
    return output, executionTime

# --- Algorithm 2 ---

# Note - Although both algorithms are O(n),
# This algorithm is much better than the previous, as all operations are done during insertion!
def checkUnique2(testList):
    dictionary = {}
    for item in testList:
        if item in dictionary:
            return False
        else:
            dictionary[item] = 1
    return True

# Algorithm Two. T(n) = 1 + 1 + n(1 + 1 + 1) + 1
    # T(n) = 3 + 3n
    # O(n)
def AlgorithmTwo(testList):
    startTime = time.time() 
    output = checkUnique2(testList)
    endTime = time.time()
    executionTime = endTime - startTime

    return output, executionTime 

# Runs 5 trials to compare the speed of the two algorithms
# Algorithm Two is really fast, so I had to change the possible range of integers to be from
# 1 to 5 million, and the length of the input at 1 million elements to see the runtime. 
# However my laptop is pretty fast,
# I don't know if that will run on your computer so I lowered it.
# Even so, the runtime for Algorithm Two is 0.0000000000 for many trials
# It should be noted that these algorithms take a lot of memory (space complexity) as a tradeoff for speed.
def runSpeedTest(n: int, start: int, stop: int, unique: bool):
    
    for trial in range(1,6):
        if unique:
            randomList = generateUniqueList(n)
        else:
            randomList = generateList(n, start, stop)
        
        outputOne, runTimeOne = AlgorithmOne(randomList)
        outputTwo, runTimeTwo = AlgorithmTwo(randomList)
        
        print("\n", "-"*50, "\n","\nTrial",trial)
        print("Algorithm One output: ", outputOne)
        print("Algorithm One runtime: %4.20f seconds" %(runTimeOne))
        print("\nAlgorithm Two output: ", outputTwo)
        print("Algorithm Two runtime: %4.20f seconds" %(runTimeTwo))


def main():
    # setting unique = True will guarantee a unique list input (worst case).
    # setting unique = False will generate a random list with possible duplicates.
    unique = False

    # input size
    n = 1000000 

    # the possible range of random numbers in each list
    randomStart = 1
    randomEnd = 1000000 

    # ^You can change these variables for testing
    runSpeedTest(n, randomStart, randomEnd, unique)


if __name__ == "__main__":
    main()
    """
    From running the speed tests, Algorithm 2 is the most efficient
    
    I think this is due to the fact that Algorithm 1 requires iterating through the entire list at least once,
    and then iterates the entire dictionary to find a duplicate (a key with a value greater than one)
    Even though the dictionary search is O(1), the two iterations can take a while if n = 1 million
    
    On the other hand, Algorithm 2 will run a dictionary search upon each insertion. This means that it can 
    return False before iterating through the whole list. And it only requires a single iteration.
    
    Algorithm One. T(n) = 1 + n(1 + 1 + 1) + 1 + n(1 + 1) + 1
    T(n) = 3 + 3n + 2n
    T(n) = 3 + 5n
    O(n)

    Algorithm Two. T(n) = 1 + 1 + n(1 + 1 + 1) + 1
    T(n) = 3 + 3n
    O(n)
    """

    

    

