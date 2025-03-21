import random
def CreateRandomList(v, L):
    A = []
    for i in range(v, L):
        A.append(random.randrange(v, L))
    return A

A = CreateRandomList(-10, 10)

a = [4, -2, 1, -3, 2, 7, -4, 6, 3, -5, 2, -1, -4, 5, -3]

def MaxSubSequence (A):
    bests = 0
    beste = 0
    bestSum = A[0]
    for s in range(0, len(A)):
        for e in range(s, len(A)):
            sum = 0
            for i in range(s, e + 1):
                sum += A[i]
            if sum > bestSum:
                bests = s
                beste = e
                bestSum = sum
    return bests, beste


def MaxSubSequences (A):
    bests = 0
    beste = 0
    bestSum = A[0]
    for s in range(0, len(A)):
        for e in range(s, len(A)):
            sum = 0
            for i in range(s, e + 1):
                sum += A[i]
            if sum > bestSum:
                bests = s
                beste = e
                bestSum = sum
    return bests, beste

print(A)
print(MaxSubSequence(A))