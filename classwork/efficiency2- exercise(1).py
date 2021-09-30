# Algorithm Efficiency
# Program measures the number of iterations
# that execute binary search for an item in a list of radomly
# generated numbers.  The size of the list is input by the
# user

import time
import math
import random
def binarySearch (alist, item):
    
    first = 0
    last = len(alist)-1
    found = False
    iterations = 0
    while first <= last and not found:
        midpoint = (first+last)//2
        iterations += 1
        if alist[midpoint]==item:
            found = True
        else:
            if item<alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found, iterations
def main():
    
    list_sz = int(input("Input list size: "))

    # Create a list of randomly generated floats
    rand_list = []
    for i in range(list_sz):
        rand_list.append(int(random.random() * 100.0))
    
    print(rand_list)
    rand_list.sort()
    print(rand_list)
    result, iterations=binarySearch(rand_list, 5)
    print("for list_size= ", list_sz, "Number of iterations= ",iterations)
    print(result)
    


main()


