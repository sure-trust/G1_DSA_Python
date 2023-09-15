class CircularQueue:
    def __init__(self, n):
        self.queue = [None] * n
        self.front, self.rear = 0, 0
        self.SIZE = 0
        self.capacity = n

    def enqueue(self, item):
        if self.SIZE < self.capacity:
            self.queue[self.rear] = item
            self.SIZE += 1
            self.rear = (self.rear + 1) % self.capacity
            return
        print("Queue is full")

    def dequeue(self):
        if self.SIZE == 0:
            print("Queue is empty")
            return
        temp = self.queue[self.front]
        self.queue[self.front] = None
        self.front += 1
        self.SIZE -= 1
        return temp

    def display(self):
        if self.SIZE != 0:
            print(self.queue)
        else:
            print("Enqueue elements to display!")


obj = CircularQueue(4)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.display()
obj.dequeue()
obj.dequeue()
obj.display()
obj.enqueue(1)
obj.enqueue(2)
obj.display()
