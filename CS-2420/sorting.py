
from createrandom import CreateRandomList


def BubbleSort(A):
    change = True
    while change:
        change = False
        for i in range(0, len(A)-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                change = True

def ShakerSort(A):
    change = True
    while change:
        change = False
        for i in range(0, len(A)-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                change = True
        for i in range(0, len(A)-2, -1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                change = True

def CountingSort(A):
    F = [0] * len(A)
    for n in A:
        F[n] += 1
    k = 0
    for i in range(len(F)):
        val = i
        count = F[i]
        for j in range(count):
            A[k] = val
            k += 1

def main():
    A = CreateRandomList(10)
    B = A.copy()
    C = A.copy()
    D = A.copy()
    print(A)
    ShakerSort(C)
    BubbleSort(B)
    CountingSort(D)
    A.sort()
    print("Built in: ", A) 
    print("Bubble: ", B)
    print("Shaker: ", C) 
    print("Counting: ", D)

main()