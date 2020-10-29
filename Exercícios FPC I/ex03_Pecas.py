import math #Para que os arrays da direita e esqueda tenham valores infinitos na funcao merge


#As funções merge e merge sort foram retiradas do livro Algoritmos: Teoria e Prática (Cormen)
def mergeSort(A,p,r):
    if p < r:
        q = (p+r)//2
        mergeSort(A,p,q)
        mergeSort(A,q+1,r)
        merge(A,p,q,r)
        
def merge(A,p, q, r):
    nL = q - p + 1
    nR = r - q
    L = [0] * (nL + 1)
    R = [0] * (nR + 1)
    for i in range(0, nL):
        L[i] = A[p + i]
    for j in range(0, nR):
        R[j] = A[q+1 + j]
    L[nL] = math.inf
    R[nR] = math.inf 
    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j =j + 1

n_pecas = int(input())
pecasTenho = [int(i) for i in input().split()]
mergeSort(pecasTenho,0,len(pecasTenho)-1)

pecasTotal = []
for i in range(1,n_pecas+1):
    pecasTotal.append(i)

for i in range(0,len(pecasTotal)):
    if int(pecasTenho[i]) == pecasTotal[i]:
        continue
    else:
        print(pecasTotal[i])
        break 