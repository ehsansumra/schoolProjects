from assignment_7 import Node, OrderedList
from random import randint

# Generate 15 random integers from values 1-5
# The OrderedList.add() method adds the integer to the linked list next to the first integer it is greater than
# This method of insertion ensures that the linked list is sorted
def genList():
    linkedList = OrderedList()
    for i in range(15):
        integer = randint(1,5)
        linkedList.add(integer)
    return linkedList

def main():
    intList = genList()
    intList.printList()

    val = intList.pop()
    intList.printList()
    print(val)

    item = intList.pop_pos(0)
    intList.printList()
    print(item)

    print(intList.count(2))
    print(intList.count(3))

    intList.unique()
    print(f"Unique List: ", end='')
    intList.printList()
    
    linkedList = OrderedList()

if __name__ == "__main__":
    main()