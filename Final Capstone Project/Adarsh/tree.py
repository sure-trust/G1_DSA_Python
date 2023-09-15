from queue import Queue


class Node:
    def __init__(self, data):
        self.data = data
        self.list = []


def create(data=int(input("Enter the root data: "))):
    root = None

    if -1 != data:
        newNode = Node(data)
        root = newNode

    else:
        return root

    pendingNode = Queue()
    pendingNode.put(root)

    while pendingNode.qsize() > 0:
        front = pendingNode.get()
        n = int(input(f"How many Children do you want to enter? : {front.data} : "))
        if n > 0:
            for i in range(n):
                data = int(input(f"Enter the children {front.data}'s data : "))
                newNode = Node(data)
                front.list.append(newNode)
                pendingNode.put(newNode)
    return root


def display(root):
    if root is None:
        return
    print("Root data:", root.data)
    pendingQueue = Queue()
    pendingQueue.put(root)

    while pendingQueue.qsize() > 0:
        front = pendingQueue.get()
        for i in range(len(front.list)):
            print("Children of:", front.data, ":", front.list[i].data, end=" | ")
            pendingQueue.put(front.list[i])
        print()


def depth_traversal(root):
    if root is None:
        return
    print("Value: ", root.data)
    for i in range(len(root.list)):
        self.depth_traversal(root.list[i])


def input_by_rec():
    root = None
    data = int(input("Enter the root data: "))
    newNode = Node(data)
    root = newNode

    n = int(input("Enter the number of children: "))

    for i in range(n):
        child = self.input_by_rec()
        if root.list[0] is None:
            root.list.pop()
        root.list.append(child)

    return root


def height(root):
    count = 0
    for i in range(len(root.list)):
        count = max(count, height(root.list[i]))
    count += 1

    return count


maxElm = None


def max_node(root):
    global maxElm
    if root is None:
        return

    if maxElm is None:
        maxElm = root

    elif root.data > maxElm.data:
        maxElm = root

    for i in range(len(root.list)):
        max_node(root.list[i])

    return maxElm.data


def count_leaf(root):
    if root is None:
        return 0

    if len(root.list) == 0:
        return 1
    ans = 0
    for i in range(len(root.list)):
        ans += count_leaf(root.list[i])

    return ans


newTree = create()
display(newTree)
print(height(newTree))
