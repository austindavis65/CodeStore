class Node:
    def __init__(self, item, nxt):
        self.item = item
        self.nxt = nxt


class LinkedList:
    def __init__(self):
        self.first = None
        self.count = 0

    def Insert(self, item):
        if self.Exists(item):
            return False
        n = Node(item, self.first)
        self.first = n
        self.count += 1
        return True
    
    def Size(self):
        current = self.first
        count = 0
        while current is not None:
            count += 1
            current = current.nxt
        return count
    
    def Retrieve(self, item):
        current = self.first
        while current is not None:
            if item == current.item:
                return current.item
            current = current.nxt
        return None

    def Delete(self, item):
        if not self.Exists(item):
            return False
        if self.first.item == item:
            self.first = self.first.nxt
            return True
        current = self.first
        while not (current.nxt.item == item):
            current = current.nxt
        current.nxt = current.nxt.nxt
        self.count -= 1
        return True

    def __iter__(self):
        current = self.first
        while current is not None:
            yield current.item
            current = current.nxt

    def Exists(self, item):
        current = self.first
        while current is not None:
            if item == current.item:
                return True
            current = current.nxt
        return False


