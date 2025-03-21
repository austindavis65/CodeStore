class Stack:
    def __init__(self):
        self.A=[]

    def push(self, item):
        self.A.append(item)

    def pop(self):
        return self.A.pop()

    def top(self):
        return self.A[-1]

    def IsEmpty(self):
        return len(self.A)==0
