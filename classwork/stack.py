
class Stack:
    
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.push(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[self.items.length - 1]

    def isEmpty(self):
        if self.items:
            return True
        else:
            return False

    def size(self):
        return len(self.items)
