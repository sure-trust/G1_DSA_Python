from math import inf


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create():
    root = None
    data = int(input("Enter the root node: "))

    if data == -1:
        return root

    newNode = Node(data)
    root = newNode

    root.left = create()
    root.right = create()

    return root


def display(root):
    if root is None:
        return

    print(root.data, end="|")

    display(root.left)
    display(root.right)


def searchBST(root, val):
    flag = False
    if not root:
        return False

    if root.data == val:
        return True

    leftSubtree = searchBST(root.left, val)

    if leftSubtree:
        flag = True

    rightSubtree = searchBST(root.right, val)

    if rightSubtree:
        flag = True

    return flag


def max_min(root):
    if not root:
        return {"max": 0, "min": inf}

    left = max_min(root.left)
    right = max_min(root.right)

    maxVal = max(left["max"], right["max"], root.data)
    minVal = min(left["min"], right["min"], root.data)

    ans = {"max": maxVal, "min": minVal}
    return ans


def sum_nodes(root):
    if not root:
        return 0

    return root.data + sum_nodes(root.left) + sum_nodes(root.right)


def delete_leaf(root, item):
    if root is None:
        return None

    root.left = delete_leaf(root.left, item)
    root.right = delete_leaf(root.right, item)

    if root.left is None and root.right is None and root.data == item:
        print(f"{root.data} node deleted.")
        del root
        return None

    return root


rootNode = create()
delete_leaf(rootNode, 2)
display(rootNode)
