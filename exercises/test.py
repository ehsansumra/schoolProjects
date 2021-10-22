class Queue:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def printQueue(self):
        for item in self.items:
            print(item, end=" ")
        print()

# Write a function extractFromQueue (k, q) that takes the element k and the queue q as input
# parameters. The function searches for the element k in q, deletes it and returns True if found and
# returns False if the element k is not found in q. Any other element must remain on the queue
# respecting their order. Write a main method to test this function.

def extractFromQueue(k, q):
    tempQ = Queue()
    match = False
    while not q.isEmpty():
        current = q.dequeue()
        if current == k:
            match = True
        else:
            tempQ.enqueue(current)

    while not tempQ.isEmpty():
        q.enqueue(tempQ.dequeue())
    
    return True

def main():
    Q = Queue()
    numList = [1,2,3,4,5,6,7,8,9]
    for num in numList:
        Q.enqueue(num)
    
    Q.printQueue()
    extractFromQueue(4, Q)
    Q.printQueue()

if __name__ == "__main__":
    main()