class TestNode {
    constructor(value) {
        this.value = value
        this.next = null
    }

    getNext() {
        return this.next
    }

    getValue() {
        return this.value
    }

    setValue(value) {
        this.value = value
    }

    setNext(next) {
        this.next = next
    }
}

class LinkedList {
    constructor(value) {
        this.head = new TestNode(value)
        this.length = 0
    }

    isEmpty() {
        return this.head === null
    }

    push(value) {
        let currentNode = this.head
        while (currentNode.next != null) {
            currentNode = currentNode.next
        }
        currentNode.next = new TestNode(value)
        this.length += 1
    }

    slowLength() {
        let count = 0
        let currentNode = this.head
        while (currentNode.next != null) {
            count += 1
            currentNode = currentNode.next
        }
        return count
    }

    print() {
        let currentNode = this.head
        while (currentNode.next != null) {
            console.log(currentNode.getValue())
            currentNode = currentNode.next
        }
    }

    some(item) {
        let currentNode = this.head
        while (currentNode.next != null) {
            if (currentNode.getValue() === item) return true;
            currentNode = currentNode.next
        }
        return false
    }

    remove(item) {
        let currentNode = this.head
        let previousNode = null
        let found = false
        let end = false

        while (!found || end) {
            if (currentNode.getNext() === null) end = true;
            if (currentNode.getValue() == item) {
                found = true
            } else {
                previousNode = currentNode
                currentNode = currentNode.getNext()
            }
        }
        
        if (found && previousNode === null) {
            this.head = currentNode.get_next()
        } else {
            if (found) previousNode.setNext(currentNode.getNext());
        }
        
    }
}

let main = () => {
    let linkedList = new LinkedList("head")
    for (let i = 0; i < 11; i++) {
        linkedList.push(i)
    }
    linkedList.print()
    console.log(linkedList.some(10))
    console.log(linkedList.length)
    linkedList.remove(4)
    linkedList.print()
}

main()