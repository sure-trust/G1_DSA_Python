import array as ary
class stack:
    def __init__ (self):
        self.Top=-1
        self.Arr=ary.array('i',[])
    def push(self,key):
        self.Top+=1
        self.Arr.append(key)
    def pop(self):
        num=self.Arr[self.Top]
        self.Arr.pop(self.Top)
        self.Top-=1
        print(self.Top)
        return num
    def isEmpty(self):
        if(self.Top==-1):
            print("Stack is underflow")
        else:
            print("Stack is not empty")
    def peek(self):
        print(self.Arr[self.Top])
    def display(self):
        for i in range(self.Top+1):
            print(self.Arr[i])
obj=stack()
n=int(input("Enter the no of elements U want to push:"))
for i in range(n):
    ele=int(input("Enter the element U wangt to push:"))
    obj.push(ele)
print("performing peek operation:")
obj.peek()
print("performing pop operation:")
obj.pop()
obj.display()
print("performing peek operation:")
obj.peek()
print("Checking whether stack is empty or not:")
obj.isEmpty()
print("Displaying the elements in the stack:")
obj.display()
    