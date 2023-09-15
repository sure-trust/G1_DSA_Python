class MinHeap:

    def __init__(self):
        self.nodes = []

    def size(self):
        return len(self.nodes)

    def parent(self, i):
        return (i - 1) // 2

    def swap(self, i, j):
        self.nodes[i], self.nodes[j] = self.nodes[j], self.nodes[i]

    def minInsert(self, key):
        child = self.size()
        self.nodes.append(key)

        while child != 0:
            p = self.parent(child)
            if self.nodes[p] > self.nodes[child]:
                self.swap(p, child)
            child = p

    def removeMin(self):
        if len(self.nodes) < 1:
            return 0

        if len(self.nodes) == 1:
            return self.nodes.pop()

        minValue = self.nodes[0]
        self.nodes[0] = self.nodes[len(self.nodes) - 1]
        self.nodes.pop()

        currentIndex = 0
        left = (currentIndex * 2) + 1
        right = (currentIndex * 2) + 2

        while currentIndex < len(self.nodes):
            if left < len(self.nodes) and right < len(self.nodes) and (self.nodes[left] < self.nodes[right]):
                if self.nodes[left] < self.nodes[currentIndex]:
                    temp = self.nodes[left]
                    self.nodes[left] = self.nodes[currentIndex]
                    self.nodes[currentIndex] = temp
                    currentIndex = left
                else:
                    break
            elif right < len(self.nodes):
                if self.nodes[right] < self.nodes[currentIndex]:
                    temp = self.nodes[right]
                    self.nodes[right] = self.nodes[currentIndex]
                    self.nodes[currentIndex] = temp
                    currentIndex = right
                else:
                    break
            else:
                break
            left = (currentIndex * 2) + 1
            right = (currentIndex * 2) + 2

        return minValue

    def displayPriorityQueue(self):
        print(self.nodes)

    def print(self):
        print(self.nodes)


obj = MinHeap()
obj.minInsert(7)
obj.minInsert(10)
obj.minInsert(4)
obj.minInsert(3)
obj.minInsert(20)
obj.minInsert(15)
obj.print()
