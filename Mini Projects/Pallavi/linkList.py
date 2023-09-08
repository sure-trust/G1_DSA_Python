class node:
    data=None
    next=None
    def __init__(self,key):
        self.data=key

class linkListFunction:
    def __init__(self):
        self.head=None
        self.tail=None

    def createLlist(self):
        datas=int(input("Enter the data:"))
        while(datas!=-1):
            if(self.head==None):
                self.head=node(datas)
                self.tail=self.head
            else:
                newnode=node(datas)
                self.tail.next=newnode
                newnode.next=None
                self.tail=self.tail.next
            datas=int(input("Enter the data:"))
        return self.head
        
    def insertAtFirst(self,data):
        if(data!=-1):
            ob=node(data)
            if(self.head!=None):
                ob.next=self.head
                self.head=ob
                return self.head
            else:
                self.head=ob
                return self.head
        return self.head
    def insertAtIndex(self,index,data):
        if(index==1):
            self.insertAtFirst(data)
            return
        if(index<=self.getLength()+1):
            newNode=node(data)
            count=1
            temp=self.head
            while(count!=index-1):
                temp=temp.next
                count+=1
            if(index==self.getLength()+1):
                temp.next=newNode
                return
            newNode.next=temp.next
            temp.next=newNode
            return
        print("invalid index")
        return head


    def deleteHead(self,head):
        if(head!=None):
            tem=self.head.next
            self.head.next=None
            del head
            self.head=tem
            return self.head
    
    def deleteTailNode(self):
        temp=self.head
        while(temp.next.next!=None):
            temp=temp.next
        del temp.next
        temp.next=None
        return self.head
    def getLength(self):
        if(self.head==None):
            return 0
        count=1
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
            count+=1
        return count

    def search(self,key):
        temp=self.head
        count=1
        while(temp!=None):
            if(temp.data==key):
                print("element is found at ",count,"index")
                return
            else:
                count+=1
                temp=temp.next
        print("element not found")
        return
    def updateList(self,index):
        temp=self.head
        count=1
        key=int(input("\nenter the updated value:"))
        if(count==index):
            temp.data=key
            return
        while(count<=index and temp!=None):
            if(count==index):
                temp.data=key
                return
            else:
                count+=1
                temp=temp.next
        print("Invalid index")

    def display(self,head):
        if(head==None):
            return
        print(head.data,end=" ")
        self.display(head.next)
    def mid(self):
        if(self.head!=None):
            count=0
            slow=self.head
            fast=self.head
            if(slow.next==None):
                return count
            elif(slow.next.next==None):
                count+=1
                return count
            while(fast!=None and fast.next!=None):
                count+=1
                slow=slow.next
                fast=fast.next.next
            return count
        print("Link list is empty")
        return 0


    
    def __reverse(self,head):
        if(head==None):
            t={'first':None,'second':None}
            return t
        temp=self.__reverse(head.next)
        if(temp['first']==None):
            temp['first']=head
            temp['second']=head
        else:
            head.next=None
            temp['second'].next=head
            temp['second']=head
        return temp

    def reverse(self):
        t=self.head
        temp=self.__reverse(t)
        return temp['first']
    def deleteIndexNode(self, index):
        if(self.head != None):
            temp = self.head
            p = self.head
            count = 1
            if(index == 1):
                self.head = self.deleteHead()
                return
            while(count != index-1):
                if(count == index-1 and temp.next.next == None):
                    del temp.next
                    temp.next = None
                    return
                if(temp.next != None):
                    temp = temp.next
                    count+=1
                else:
                    print('Your index is invalid ')
                    return
            if(temp.next.next != None):
                p = temp.next.next
                del temp.next
                temp.next = p
            else:
                del temp.next
                temp.next = None
        else:
            print("linklist is empty")
            return -1
    def removeDuplicates(self):
        if(self.head!=None):
            temp=self.head
            count=1
            while(temp!=None and temp.next!=None):
                if(temp.data==temp.next.data):
                    count+=1
                    self.deleteIndexNode(count)
                    temp=temp.next
                    count-=1
                else:
                    count+=1
                    temp=temp.next
            return self.head
        else:
            print("List is empty")
            return head

obj=linkListFunction()
H=obj.createLlist()
obj.display(H)
s=int(input("\nEnter the element you want to search:"))
obj.search(s)
ind=int(input("\nEnter the index value you want to update:"))
obj.updateList(ind)
obj.display(H)
num=int(input("\nenter the element to insert before head:"))
H=obj.insertAtFirst(num)
obj.display(H)
print("\nlength of Linklist:",obj.getLength())
index=int(input("enter the index U want to insert:"))
data=int(input("Enter the value:"))
obj.insertAtIndex(index,data)
obj.display(H)
print("\nmid value:",obj.mid())
d=int(input("\nEnter the index you want to delete:"))
h=obj.deleteIndexNode(d)
obj.display(h)
print("Deleting tail node:")
h=obj.deleteTailNode()
obj.display(h)
print("\nRemoving the duplicate values")
h=obj.removeDuplicates()
obj.display(h)
print("\nrevresing the linked list:")
H=obj.reverse()
obj.display(H)
print()

