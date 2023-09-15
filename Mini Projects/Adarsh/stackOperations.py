class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def overflow(self):
        if self.top == len(self.stack):
            return True
        else:
            return False

    def underflow(self):
        if self.top == -1:
            return True
        else:
            return False

    def pop(self):
        if not self.underflow():
            self.stack.pop(self.top)
            self.top -= 1

    def push(self, element):
        if not self.overflow():
            self.top += 1
            self.stack.append(element)

    def peek(self):
        if not self.underflow():
            return self.stack[self.top]


obj = Stack()
