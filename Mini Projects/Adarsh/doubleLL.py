class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def create(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            newNode.next = self.head
            newNode.prev = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = newNode
            newNode.prev = current
            newNode.next = self.head
            self.head.prev = newNode

    def display(self):
        if not self.head:
            print("The list is empty.")
        else:
            current = self.head
            while True:
                print(current.data, "|", sep="", end="")
                current = current.next
                if current == self.head:
                    break
            print()


obj = DoublyLinkedList()
obj.create(1)
obj.create(2)
obj.create(3)
obj.display()
