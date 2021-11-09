from RecBinarySearch import binary_search
from OrderedSequential import ordered_sequential_search
from Sequential import sequential_search


def searchTester(searchFunc, searchlist: list, searchItems: list):
    for item in searchItems:
        print("Searching for", item)
        print(searchFunc(searchlist, item))

if __name__ == "__main__":
    myList = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    myListOrdered = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    searchItems = [3, 13]
    
    print("\nBinary Search on", myListOrdered)
    searchTester(binary_search, myListOrdered, searchItems)
    
    print("\nOrdered Sequential Search on", myListOrdered)
    searchTester(ordered_sequential_search, myListOrdered, searchItems)
    
    print("\nSequential Search", myList)
    searchTester(sequential_search, myList, searchItems)
