class Stack:
    def __init__(self):
        self.items = []

    def IsEmpty(self):
        return self.items == []

    def Push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def Top(self):
        return self.items[-1]
    