class Deque:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def add_front(self, item):
        self.items.append(item)
    def add_rear(self, item):
        self.items.insert(0,item)
    def remove_front(self):
        return self.items.pop()
    def remove_rear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)        
    
def isPalindrome(word: str):
    deque = Deque()
    for letter in word:
        deque.add_front(letter)
    
    while deque.size() > 1:
        front = deque.remove_front()
        rear = deque.remove_rear()
        if not(rear == front):
            return False
    
    return True

def main():
    words = ["radar", "mom", "raddar", "momm", "mmomm", "mmoomm", "hello"]
    for word in words:
        print(word, isPalindrome(word))

if __name__ == "__main__":
    main()