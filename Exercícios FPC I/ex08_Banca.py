import math #Usada apenas na funcao merge (math.inf)

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

#substituir o "if x in array" do python           
def contem(a,b):
    for i in range(0,len(a)):
        if a[i] == b:
            return True
    return False


#====================================================#
while True:
  try:
    A , B = [int(i) for i in input().split()]
    saldo_atual = []
    saldo_atual = list(map(int, input()))

    saldo_ord = saldo_atual[:] #copia a lista
    mergeSort(saldo_ord,0,(A-1))#ordena a lista
    menores = saldo_ord[:B]

    i = j = 0
    saldo = ""
    while True:
      if i == B or j == A:
        break
      else:
        if contem(menores,saldo_atual[j]):
          saldo_atual[j] = 'x'
          i +=1
          j +=1
        else:
          j += 1 
     
    saldo = ''
    for i in range(0,A):
       if saldo_atual[i] != 'x':
          saldo += str(saldo_atual[i])
            
    print(saldo)
  except:
    break