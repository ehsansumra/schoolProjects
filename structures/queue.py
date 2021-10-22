class Queue:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
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
       
def main(names, num):
    playerQueue = Queue()
    for name in names:
        playerQueue.enqueue(name)
    playerQueue.printQueue()

    while playerQueue.size() > 1:
        for i in range(num):
            front = playerQueue.dequeue()
            playerQueue.enqueue(front)
            playerQueue.printQueue()
        playerQueue.dequeue()
        
    playerQueue.printQueue()

if __name__ == "__main__":
    num = 5
    names = ["Brad", "Kent", "Jane", "Susan", "Bill"]
    main(names, num)
 
