from bst import *


def insert(root, value):
    if root is None:
        newNode = Node(value)
        root = newNode
        return root

    if value < root.val:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root


def update(root, key, value):
    if not root:
        return root

    if root.val == key:
        root.val = value

    if key < root.val:
        root.left = update(root.left, key, value)
    else:
        root.right = update(root.right, key, value)

    return root


def delete(root, key):
    if not root:
        return None

    if key < root.val:
        root.left = delete(root.left, key)
        return root

    elif key > root.val:
        root.right = delete(root.right, key)
        return root

    else:
        if root.left is None and root.right is None:
            del root
            return None

        elif root.left is None:
            temp = root.right
            del root
            return temp

        elif root.right is None:
            temp = root.left
            del root
            return temp

        else:
            temp = root.right
            minNode = root.right

            while minNode.left is not None:
                minNode = minNode.left

            minNode.left = root.left
            del root
            return temp


def insert_duplicate(root, item):
    if not root:
        return None

    if root.val == item:
        newNode = Node(item)
        newNode.right = root.right
        root.right = newNode

        return root

    elif item < root.val:
        insert_duplicate(root.left, item)
    else:
        insert_duplicate(root.right, item)

    return root


nodes = [5, 3, 1, 0, -1, -1, 2, - 1, - 1, 4, -1, -1, 13, 11, -1, -1, 15, 14, 12, -1, -1, -1, 16, -1, -1]
nodes.reverse()
rootNode = create(nodes)
display(rootNode)
print("\n")

insert_duplicate(rootNode, 4)
display(rootNode)
