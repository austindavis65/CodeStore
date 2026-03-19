from createrandom import CreateRandomList
import sys
def MergeSort(A):
    if len(A) <= 1:
        return
    
    mid = len(A) // 2
    L = A[:mid]
    R = A[mid:]

    MergeSort(L)
    MergeSort(R)

    k=i=j=0

    while i < len(L) and j < len(R):
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
    
def QuickSort(A, low, high):
    if high-low<= 0:
        return
    lmgt = low+1
    for i in range(low+1, high+1):
        if A[i] < A[low]:
            A[i],A[lmgt] = A[lmgt],A[i]
            lmgt += 1
    pivot = lmgt - 1
    A[pivot], A[low] = A[low], A[pivot]
    QuickSort(A, low, pivot-1)
    QuickSort(A, pivot+1, high)

def ModifiedQuickSort(A, low, high):
    if high-low<= 0:
        return
    mid = (low+high)//2
    A[low],A[mid]=A[mid],A[low]
    lmgt = low+1
    for i in range(low+1, high+1):
        if A[i] < A[low]:
            A[i],A[lmgt] = A[lmgt],A[i]
            lmgt += 1
    pivot = lmgt - 1
    A[pivot], A[low] = A[low], A[pivot]
    ModifiedQuickSort(A, low, pivot-1)
    ModifiedQuickSort(A, pivot+1, high)

    



def main():
    sys.setrecursionlimit(5000)

    A =  CreateRandomList(10)
    B = A.copy()
    C = A.copy()
    D = A.copy()
    print(A)
    A.sort()
    print("Built in: ", A)
    MergeSort(C)
    print("Merge: ", C)
    QuickSort(B, 0, len(B)-1)
    print("Quick: ", B)
    ModifiedQuickSort(D, 0, len(D)-1)
    print("Modified: ", D)

main()