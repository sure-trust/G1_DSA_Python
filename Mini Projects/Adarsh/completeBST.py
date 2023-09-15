from bst import Node


def create():
    data = int(input("Enter the data: "))

    if data == -1:
        return None

    newNode = Node(data)
    root = newNode

    q = [root]

    while len(q) > 0:
        front = q.pop(0)

        data = int(input("Enter the data : "))
        if data == -1:
            return root
        newNode = Node(data)
        q.append(newNode)
        front.left = newNode

        data = int(input("Enter the data : "))
        if data == -1:
            return root
        newNode = Node(data)
        q.append(newNode)
        front.right = newNode


def delete_leaf(root, elm):
    q = [root]
    while len(q):
        temp = q.pop(0)
        if temp is elm:
            temp = None
            return
        if temp.right:
            if temp.right is elm:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is elm:
                temp.left = None
                return
            else:
                q.append(temp.left)


def delete(root, key):
    if root is None:
        return None
    if root.left is None and root.right is None:
        if root.val == key:
            return None
        else:
            return root
    key_node = None
    q = [root]
    temp = None
    while len(q):
        temp = q.pop(0)
        if temp.val == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    if key_node:
        x = temp.val
        delete_leaf(root, temp)
        key_node.val = x
    return root


def bfs(root):
    if not root:
        return

    q = [root]

    while len(q) > 0:
        print(q[0].val, end="|")
        front = q.pop(0)

        if front.left is not None:
            q.append(front.left)

        if front.right is not None:
            q.append(front.right)


newRoot = create()
bfs(newRoot)

value = int(input("\nEnter the data to be deleted: "))
deleteData = delete(newRoot, value)
print("\nThe deleted node is:", deleteData.val)
bfs(newRoot)
