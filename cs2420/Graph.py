from createrandom import CreateSortedList

class MyQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item): #adds item to the end of the queue and returns true
        self.queue.append(item)
    
    def dequeue(self): #pops the first item in the queue and returns it.
        if not self.IsEmpty():
            return self.queue.pop(0)

    def IsEmpty(self): #returns a true or false if empty or not
        if self.queue == []:
            return True
        return False
    
    def __iter__(self):
        for item in self.queue:
            yield item


class Graph:
    def __init__(self, numVertices):
        self.neighbors = []
        for i in range(numVertices):
            self.neighbors.append([])

    def AddEdge(self, v0, v1):
        self.neighbors[v0].append(v1)
        self.neighbors[v0].sort()
    
    def IsEdge(self, v0, v1):
        return v1 in self.neighbors[v0]

    def FindNeighbors(self, v):
        return self.neighbors[v]
    
    def FindPath(self, v0, v1):
        From = [-1] * len(self.neighbors)
        From[v0] = v0
        queue = MyQueue()
        queue.enqueue(v0)
        while not queue.IsEmpty():
            c = queue.dequeue()
            if c == v1:
                path = [c]
                while From[c] != c:
                    c = From[c]
                    path.append(c)
                path.reverse()
                return path
            for n in self.neighbors[c]:
                if From[n] == -1:
                    queue.enqueue(n)
                    From[n] = c

    def __iter__(self):
        for item in self.neighbors:
            yield item



# c = MyQueue()
# A = CreateSortedList(10)
# print(A)
# b = []
# for i in range(len(A)):
#     c.enqueue(A[i])
# t = c.dequeue()
# b.append(t)
# t = c.dequeue()
# b.append(t)
# print(c)
# print(b)

def main():
    fin = open('graph.txt','r')
    numVertices = int(fin.readline())
    g = Graph(numVertices)
    numedges = int(fin.readline())
    for i in range(numedges):
        line = fin.readline()
        words = line.split()
        g.AddEdge(int(words[0]),int(words[1]))
    
    numtests = int(fin.readline())
    for i in range(numtests):
        line = fin.readline()
        words = line.split()
        path = g.FindPath(int(words[0]),int(words[1]))
        print(path)
    fin.close()

main()