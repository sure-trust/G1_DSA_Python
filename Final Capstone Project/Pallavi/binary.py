from collections import deque
from queue import Queue

class BinaryNode:
    data=0
    left=None
    right=None
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinaryFunctions:
    def __init__(self):
        self.s=0

    def createBinaryTree(self):
        root=None
        data=int(input("enter the data:"))
        if(data==-1):
            return root
        newTreeNode = BinaryNode(data)
        root = newTreeNode
        print("enter left child for :",root.data,":")

        root.left = self.createBinaryTree()
        print("enter right child for :",root.data,":")
        root.right = self.createBinaryTree()
        return root
    def displayLevelWise(self,root):
        if(root == None):
            return None
        
        
        print("Root Data : ",root.data)
        pendingNode = Queue() 
        pendingNode.put(root)

        while(pendingNode.qsize() > 0):
            front = pendingNode.get()
            if(front.left!=None):
                print("Left Children of :",front.data," :",front.left.data, end=" ")
                pendingNode.put(front.left)

            if(front.right!=None):  
                print("Right Children of :",front.data,": ",front.right.data, end=" ")
                pendingNode.put(front.right)
        return root
    def inorder(self,root):
        if(root==None):
            return root
        self.inorder(root.left)
        print(root.data,end='-')
        self.inorder(root.right)
        return root
    def preorder(self,root):
        if(root==None):
            return root
        print(root.data,end='-')
        self.preorder(root.left)
        self.preorder(root.right)
        return root
    def postorder(self,root):
        if(root==None):
            return root
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data,end='-')
        return root
    
        
    def searchNode(self,root,key):
        if(root == None):
            return
        
        pendingNode = Queue() 
        pendingNode.put(root)

        while(pendingNode.qsize() > 0):
            front = pendingNode.get()
            if(front!=None):
                if(front.data==key):
                    return True
                else:
                    pendingNode.put(front.left)
                    pendingNode.put(front.right)
        return False
    def searchRecur(self,root,key):
        if(root!=None):
            if(root.data==key):
                return True
            left=self.searchRecur(root.left,key)
            right=self.searchRecur(root.right,key)
            if(left==True or right==True):
                return True
            else:
                return False
        else:
            return False

    
        
    def deleteLeaf(self,root,key):
        if(root==None):
            return
        if(root.data==key and root.left==None and root.right==None):
            print("deleted leaf node:",root.data)
            del root
            return None
        root.left=self.deleteLeaf(root.left,key)
        root.right=self.deleteLeaf(root.right,key)
        return root
    def sum(self,root):
        if(root!=None):
            self.s=self.s+root.data
            self.sum(root.left)
            self.sum(root.right)
        else:
            return 0
        return self.s
    def heightOfTree(self,root):
        if(root == None):
            return 0

        return max(self.heightOfTree(root.left)+1, self.heightOfTree(root.right)+1)
    def isBalancedTree(self,root):
        if(root == None):
            return True

        leftAns = self.isBalancedTree(root.left)
        rightAns = self.isBalancedTree(root.right)

        if(leftAns and rightAns):
            if(abs(self.heightOfTree(root.left) - self.heightOfTree(root.right) <= 1)):
                return True
            else:
                return False
            
        
        return False

    
        
    

        

            
print("Creation of binary tree:")
obj=BinaryFunctions()
r=obj.createBinaryTree()
print("Inorder Tree Traversal:")
root=obj.inorder(r)
print("\nPreorder Tree Traversal:")
r=obj.preorder(root)
print("\nPostorder Tree Traversal:")
root=obj.postorder(r)
print("\nDisplaying level wise")
r=obj.displayLevelWise(root)
print("\nDeleting a leaf node:")
l=int(input("enter the leaf node:"))
r=obj.deleteLeaf(r,l)
root=obj.displayLevelWise(r)
print("\nChecking tree is balanced or not")
print(obj.isBalancedTree(root))
'''print("\nsum of the nodes in the binary tree:")
print("sum:",obj.sum(root))
root=obj.displayLevelWise(r)
s=int(input("Enter the element to be search:"))
print(obj.searchRecur(root,s))'''

class pair:
    def __init__(self, first = 0, second = 0):
        self.first = first
        self.second = second

import math
def findMaxAndMinNode(root):
    if(root == None):
        p1 = pair(0,math.inf)
        # p1.first = 0
        # p1.second = math.inf
        return p1
    
    leftAns = findMaxAndMinNode(root.left)
    rightAns = findMaxAndMinNode(root.right)
    Vmax =  max(leftAns.first, rightAns.first, root.data)
    Vmin = min(leftAns.second, rightAns.second, root.data)
    ans = pair(Vmax, Vmin)
    return ans


print("Finding maximum and minimum node:")
ob = BinaryFunctions()
root = ob.createBinaryTree()
root=ob.displayLevelWise(root)
ans = findMaxAndMinNode(root)
print()
print('max and min : ', ans.first," ",ans.second)


    


