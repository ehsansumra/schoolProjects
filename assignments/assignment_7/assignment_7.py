from random import randint
class Node:
    '''
    Create a Node object and initialize its data.  
    '''

    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    '''
    Accessor for node data
    '''

    def get_data(self):
        return self.data

    '''
    Accessor for next reference
    '''

    def get_next(self):
        return self.next

    '''
    Mutator for node data
    '''

    def set_data(self, new_data):
        self.data = new_data

    '''
    Mutator for next reference
    '''

    def set_next(self, new_next):
        self.next = new_next


class OrderedList:
    '''
    List is empty upon creation and the head reference is None
    '''

    def __init__(self):
        self.head = None

    '''
    Returns True if list is empty, False otherwise
    '''

    def is_empty(self):
        return self.head == None

    '''
    Add an element to head of the list
    '''

    def add(self, item):
        # keep track of current and previous elements
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            # if we have a match, stop
            if current.get_data() > item:
                stop = True
            # otherwise advance current and next references
            else:
                previous = current
                current = current.get_next()

        # Create a node using item as its data
        temp = Node(item)
        if previous == None:
            temp.set_next(current)
            self.head = temp
            # the element to be deleted is not the head
        else:
            temp.set_next(current)
            previous.set_next(temp)

    '''
    Returns the size of the list
    '''

    def size(self):
        # start at the head of the list
        current = self.head
        count = 0
        # Traverse the list one element at a time.  We know
        # we reached the end when the next reference is None
        while current != None:
            count = count + 1
            current = current.get_next()
        return count

    '''
    Search for an item in the list.  Returns True if found, False otherise.  
    '''

    def search(self, item):
        current = self.head
        found = False
        stop = False
        # As long as the element is not found and we haven't
        # reached the end of the list
        while current != None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    # go to the next element
                    current = current.get_next()
        return found

    '''
    Remove the first occurrence of item from the list.  
    '''

    def remove(self, item):
        # keep track of current and previous elements
        current = self.head
        previous = None
        found = False
        # traverse the list
        while current != None and not found:
            # if we have a match, stop
            if current.get_data() == item:
                found = True
            # otherwise advance current and next references
            else:
                previous = current
                current = current.get_next()

        # the element to be deleted is the head of the list
        if found:
            if previous == None:
                self.head = current.get_next()
                # the element to be deleted is not the head
            else:
                previous.set_next(current.get_next())

    # Pops an item from the linked list based on the position entered as a parameter.
    # Handles the case of an empty list, position 0,  and all other positions
    def pop_pos(self, pos):
        current = self.head
        previous = None
        invalidPos = False

        if not self.head:
            return None

        if pos == 0:
            # special case
            item = current.get_data()
            self.head = current.get_next()
            return item

        # Navigates to the Node that the pos parameter specified
        # If the pos goes beyond the linked list, it will not remove any items and return None
        for i in range(pos):
            if current.get_next():
                previous = current
                current = current.get_next()
            else:
                invalidPos=True
                
        if invalidPos:
            return None
        else:
            item = current.get_data()
            previous.set_next(current.get_next())
            return item
        
    # Iterates to the last element of the linked list, removes the Node and returns the value
    def pop(self):
        current = self.head
        previous = None
        last = False

        # Handles the case of self.head being empty
        if not self.head:
            return None

        while current != None and not last:

            if current.get_next() == None:
                last = True
            else:
                previous = current
                current = current.get_next()

        previous.set_next(None)
        return current.get_data()

    # Simply iterates until the first occurence of the item is found
    # increments the index field for each iteration, returns that field when the item is found.
    def index(self, item):

        current = self.head
        found = False
        index = -1

        while current != None and not found:
            index += 1
            if current.get_data == item:
                found == True
            else:
                current = current.get_next()
        return index

    # By using a dictionary, we can get the number of occurences for each item in the linked list
    # Each item in the dictionary uses this format:
    # {key= number : value= # occurrences}
    def count(self):
        countMap = {}

        current = self.head

        while current != None:
            num = current.get_data()
            if num in countMap:
                countMap[num] += 1
            else:
                countMap[num] = 1
            
            current = current.get_next()

        return countMap
        
    # This function takes the ordered list and returns an ordered list with no duplicate items.
    def unique(self):
        # this implementation works for ordered lists, because the duplicate items are always next to each other, in order.
        current = self.head
        previous = None

        while current != None:

            # If the previous item and the current item is equal, the current item is removed
            # by setting previous.next equal to current.next
            if previous and previous.get_data() == current.get_data():
                previous.set_next(current.get_next())
                current = current.get_next()

            # If not, there is no duplicate, continue iterating.
            else:
                previous = current
                current = current.get_next()

    
    # Print the linked list in Python list format
    def printList(self):
        current = self.head
        listStr = '['
        while current != None:
            item = str(current.get_data())
            listStr += item
            if current.get_next() != None:
                listStr += ', '
            current = current.get_next()
        print(listStr+']')

def genList():
    linkedList = OrderedList()
    for i in range(15):
        integer = randint(1,5)
        linkedList.add(integer)
    return linkedList

def main():
    # Generate an ordered linked list of 15 random integers from range 1 to 5
    intList = genList()
    # Display the generated linked list
    print("Generated Linked List: ", end="")
    intList.printList()

    # pop the last item from the linked list
    val = intList.pop()
    print("Pop from end: ", end="")
    intList.printList()
    print("Pop returned:", val)

    # pop an item by specifying its position in the linked list
    pos = 3
    item = intList.pop_pos(pos)
    print(f"Pop position {pos}: ", end="")
    intList.printList()
    print("Pop returned:", item )

    # display the count of items in the linked list
    # note that this is called after two items are popped from the linked list
    counts = intList.count()
    print(f"Occurrences:", counts)

    # remove duplicate items in the linked list
    intList.unique()
    print(f"Unique List: ", end='')
    intList.printList()
    
    linkedList = OrderedList()

if __name__ == "__main__":
    main()