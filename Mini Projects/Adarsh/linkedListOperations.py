class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data


class LinkedListFunction:
    def __init__(self):
        self.head = None
        self.tail = None

    def create(self):
        datas = int(input("Enter the data : "))
        while datas != -1:
            if self.head is None:
                self.head = Node(datas)
                self.tail = self.head
            else:
                newNode = Node(datas)
                self.tail.next = newNode
                self.tail = self.tail.next
            datas = int(input("Enter the data : "))
        return self.head

    def display(self, head):
        if head is None:
            return
        print(head.data, " ", end="")
        self.display(head.next)

    def print_reverse(self, head):
        if head is None:
            return
        self.display(head.next)
        print(head.data, " ", end="")

    def delete_head(self):
        temp = self.head
        if temp is not None:
            self.head = temp.next
            temp.next = None
            del temp
            return self.head

    def delete(self):
        item = int(input("\n\nEnter the element you want to delete: "))
        if self.head is not None:
            temp = self.head
            p = self.head

            if temp.next is None:
                if temp.data == item:
                    self.head = self.delete_head()
                else:
                    print("The entered item is not valid!")

            elif temp.next is not None and temp.data is item:
                self.head = self.delete_head()

            else:
                temp = temp.next
                while temp.next is not None:
                    if temp.data == item:
                        p.next = temp.next
                        del temp
                        return

                    p = p.next
                    temp = temp.next

                    if temp.next is None and temp.data == item:
                        del temp
                        p.next = None
                        return

                print("\nInvalid key")

    def search(self, key):
        temp = self.head
        idx = -1

        while temp is not None:
            if temp.data == key:
                idx += 1
                return "Element found at " + str(idx)
            idx += 1
            temp = temp.next

        return "\nElement not found!"

    def insert_first(self, item):
        if item != -1:
            objc = node(item)
            if self.head is None:
                self.head = objc
                return
            else:
                objc.next = self.head
                self.head = objc
                return
        return -1

    def __length(self):
        if self.head is None:
            return 0

        temp = self.head
        count = 1
        while temp.next is not None:
            temp = temp.next
            count += 1

        return count

    def insert(self, item, pos):
        if pos == 1:
            self.insert_first(item)
            return

        if pos <= self.__length():
            new_node = Node(item)
            count = 1
            temp = self.head
            while count != pos - 1:
                temp = temp.next
                count += 1

            if pos == self.__length():
                temp.next = new_node
                return

            new_node.next = temp.next
            temp.next = new_node
            return
        print("Invalid index")
        return -1


obj = LinkedListFunction()
newHead = obj.create()
obj.display(newHead)

# For head node deletion
obj.delete()
newHead = obj.head
print("\nThe List after deletion: ")
obj.display(newHead)
print("\n")

# For deletion of a key element in the linked list
obj.delete()
print("\nThe List after deletion: ")
obj.display(newHead)
print("\n")

# For searching a key
print("The linked list is: ")
obj.display(newHead)
print("\n")
k = int(input("Enter the key to search in the linked list: "))
print(obj.search(k))

# For insertion at the front of the linked list

obj.display(newHead)
obj.insert_first(int(input("Enter item to insert at the front of the linked list: ")))

# For insertion at random position

i = int(input("Enter the value to insert: "))
index = int(input("Enter the position to insert at: "))
obj.insert(i, index)
obj.display(newHead)
