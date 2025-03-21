import random
def CreateRandomList(L):
    A = []
    for i in range(L):
        A.append(random.randrange(0, L))
    return A

def CreateSortedList(L):
    A = []
    for i in range(L):
        A.append(random.randrange(0, L))
    A.sort()
    return A

def CreateRandomUniqueList(L):
    A = []
    while len(A) != L:
        for i in range(L):
            r = random.randrange(0, L)
            if r not in A:
                A.append(r)
    return A

def CreateUniqueSortedList(L):
    A = []
    while len(A) != L:
        for i in range(L):
            r = random.randrange(0, L)
            if r in A:
                pass
            else:
                A.append(r)
    A.sort()
    return A

def CreateBagList(size):
    A=[]
    bag = []
    for i in range(size):
        bag.append(i)
    for i in range(size):
        r = random.randrange(0,len(bag))
        A.append(bag[r])
        bag[r]=bag[len(bag)-1]
        bag.pop()
    return A

def CreateShuffleList(size):
    A = list(range(size))
    #random.shuffle(A)
    for i in range(size):
        r = random.randrange(0,size)
        A[i],A[r]=A[r],A[i]
    return A