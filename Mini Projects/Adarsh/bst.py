class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def create(items):
    root = None
    data = items.pop()
    if data == -1:
        return root
    newNode = Node(data)
    root = newNode

    root.left = create(items)
    root.right = create(items)

    return root


def display(root):
    if root is None:
        return

    print(root.val, end="|")

    display(root.left)
    display(root.right)


# nodes = [3, 2, -1, -1, 7, 4, -1, -1, 8, -1, -1]
# nodes.reverse()
# rootNode = create(nodes)
# display(rootNode)
