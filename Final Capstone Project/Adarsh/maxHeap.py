class MaxHeap:

    def __init__(self):
        self.nodes = []

    def size(self):
        return len(self.nodes)

    def parent(self, i):
        return (i - 1) // 2

    def swap(self, i, j):
        self.nodes[i], self.nodes[j] = self.nodes[j], self.nodes[i]

    def Insert(self, key):
        child = self.size()
        self.nodes.append(key)

        while child != 0:
            p = self.parent(child)
            if self.nodes[p] < self.nodes[child]:
                self.swap(p, child)
            child = p

    def removeMax(self):
        if len(self.nodes) < 1:
            return 0

        if len(self.nodes) == 1:
            return self.nodes.pop()

        maxValue = self.nodes[0]
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

        return maxValue

    def displayPriorityQueue(self):
        print(self.nodes)

    def print(self):
        print(self.nodes)


obj = MaxHeap()
obj.Insert(7)
obj.Insert(10)
obj.Insert(4)
obj.Insert(3)
obj.Insert(20)
obj.Insert(15)
obj.print()
