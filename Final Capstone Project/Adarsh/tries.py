class TrieNode:
    def __init__(self, data):
        self.data = data
        self.child = [None] * 26
        self.finish = False


class Trie:
    def __init__(self):
        self.root = TrieNode('\0')

    def __insert(self, root, word):
        if word == '':
            root.finish = True
            return

        index = ord(word[0]) - ord('a')
        if root.child[index] is None:
            newNode = TrieNode(word[0])
            root.child[index] = newNode
        self.__insert(root.child[index], word[1:])

    def insertWord(self, word):
        self.__insert(self.root, word)

    def __searchWord(self, root, word):
        if word == "":
            return root.finish

        index = ord(word[0]) - ord('a')
        if root.child[index] is None:
            return False

        return self.__searchWord(root.child[index], word[1:])

    def searchWord(self, word):
        return self.__searchWord(self.root, word)


ob = Trie()
ob.insertWord("alcohol")
print(ob.searchWord("alcohol"))
