import sys
import math
import random


def CreateRandomList(L):
    A = []
    for i in range(L):
        A.append(random.randrange(0, L))
    return A


def CreateMostlySortedR(L):
    A = CreateRandomList(L)
    A.sort()
    b = random.randrange(0, L)
    A[0], A[b] = A[b], A[0] 
    return A  


def CreateMostlySorted(L):
    A = CreateRandomList(L)
    A.sort()
    b = len(A)-1
    A[0], A[b] = A[b], A[0] 
    return A  


class Counter:
    def __init__(self):
        self.count=0


def BubbleSort(A, c):
    change = True
    while change:
        change = False
        for i in range(0, len(A)-1):
            c.count+=1
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                change = True


def ShakerSort(A, c):
    change = True
    while change:
        change = False
        for i in range(0, len(A)-1):
            c.count+=1
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                change = True
        for i in range(0, len(A)-2, -1):
            c.count+=1
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                change = True


def MergeSort(A, c):
    if len(A) <= 1:
        return
    
    mid = len(A) // 2
    L = A[:mid]
    R = A[mid:]

    MergeSort(L, c)
    MergeSort(R, c)

    k=i=j=0

    while i < len(L) and j < len(R):
        c.count+=1
        if L[i] <= R[j]:
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j+=1
        k+=1
    
    while i < len(L):
        A[k] = L[i]
        i+=1
        k+=1

    while j < len(R):
        A[k] = R[j]
        j+=1
        k+=1


def CountingSort(A,c):
    c.count = len(A)

   
def QuickSort(A, c):
    low = 0
    high = len(A)-1
    QuickSortR(A, c, low, high, False)


def ModQuickSort(A, c):
    low = 0
    high = len(A)-1
    QuickSortR(A, c, low, high, True)


def QuickSortR(A, c, low, high, mod):
    if high-low<= 0:
        return
    
    if mod:
        mid=(low+high)//2
        A[low],A[mid] = A[mid],A[low]
    lmgt = low+1
    for i in range(low+1, high+1):
        c.count+=1
        if A[i] < A[low]:
            A[i],A[lmgt] = A[lmgt],A[i]
            lmgt += 1
    pivot = lmgt - 1
    A[pivot], A[low] = A[low], A[pivot]
    QuickSortR(A, c, low, pivot-1, mod)
    QuickSortR(A, c, pivot+1, high, mod)


def mainrandom():
    sys.setrecursionlimit(5000)
    sorts = [BubbleSort, ShakerSort, CountingSort, QuickSort, ModQuickSort, MergeSort]
    for s in range(3, 13):
        size = 2**s
        print(s, end=" ")
        for sort in sorts:
            A = CreateRandomList(size)
            #B=A[:]
            c=Counter()
            #B.sort()
            sort(A,c)
            if c.count == 0:
                print(0, end=" ")
            else:    
                print(" ", round(math.log(c.count,2), 2), end=" ")
        print('\n')


def mainsorted():
    sys.setrecursionlimit(5000)
    sorts = [BubbleSort, ShakerSort, CountingSort, QuickSort, ModQuickSort, MergeSort]
    for s in range(3, 13):
        size = 2**s
        print(s, end=" ")
        for sort in sorts:
            A = CreateMostlySorted(size)
            #B=A[:]
            c=Counter()
            #B.sort()
            sort(A,c)
            if c.count == 0:
                print(0, end=" ")
            else:    
                print(" ", round(math.log(c.count,2), 2), end=" ")
        print('\n')


print('\n', "Sorted", '\n')
mainsorted()
print("Random", '\n')
mainrandom()