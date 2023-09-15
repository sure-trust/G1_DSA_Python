class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        newNode = Node(data)

        if not self.head:
            self.head = self.tail = newNode
            newNode.next = self.head

        else:
            self.tail.next = newNode
            self.tail = newNode
            self.tail.next = self.head

    def display(self):
        if not self.head:
            print("The circular linked list is empty")
            return
        else:
            current = self.head
            print(current.data, " ")
            while current.next is not self.head:
                current = current.next
                print(current.data, "", end="")


obj = CircularLinkList()
obj.insert(1)
obj.insert(2)
obj.display()
