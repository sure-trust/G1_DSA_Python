
class Queue:
    def __init__(self,size):
        self.queue=[None]*size
        self.front=0
        self.rear=0
        self.size=0
        self.cap=size
    def enqueue(self,key):
        if(self.size<self.cap):
            self.queue[self.rear]=key
            self.size+=1
            self.rear=(self.rear+1)%self.cap
            return
        else:
            print("Queue is Full")
    def dequeue(self):
        if(self.size<=0):
            print("Queue is empty")
            return
        else:
            data=self.queue[self.front]
            self.queue[self.front]=None
            self.front=(self.front+1)%self.cap
            self.size-=1
            return data
           
    def display(self):
        if(self.size!=0):
            print(self.queue)

obj=Queue(5)
print("Performing Enqueue operation:")
obj.enqueue(5)
obj.enqueue(6)
obj.enqueue(7)
obj.enqueue(9)
obj.enqueue(11)
obj.display()
print("Performing Dequeue operation")
obj.dequeue()
obj.dequeue()
obj.dequeue()
obj.dequeue()
obj.enqueue(1)
obj.dequeue()
obj.dequeue()
obj.enqueue(1)
obj.display()





