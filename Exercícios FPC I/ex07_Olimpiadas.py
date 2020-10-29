# Exercício 8 - Olimpíadas

#=========================================

#Código de ordenação da função ordenarPorMedalhas foi inspirado no Insertion sort
#do livro "Problem Solving with Algorithms and Data Structures using Python"
#além de ser modificado para atender a questão.
#Já a função naoContem é usada para substituir o "not in" do python
def ordenarPorMedalhas(arr): 
    for i in range(1, len(arr)): 
        key = int(arr[i][1])
        eKey = arr[i]
        j = i-1
        while j >=0 and key > int(arr[j][1]) : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = eKey

def naoContem(a,b):
    for i in range(0,len(a)):
        if a[i] == b:
            return False
    return True
#====================================


N, M = [int(x) for x in input().split(" ")]
medalhas = []
for i in range(0,N):
  medalhas.append([0,0,0])

for i in range(0,M):
  O, P, B = [int(x) for x in input().split(" ")]
  medalhas[O-1][0] = (medalhas[O-1][0]+1)
  medalhas[P-1][1] = (medalhas[P-1][1]+1)
  medalhas[B-1][2] = (medalhas[B-1][2]+1)

paises = []
Ouro = []
Prata = []
Bronze = []

for i in range(0,N):
    Ouro.append((i,medalhas[i][0]))
ordenarPorMedalhas(Ouro)
for i in range(0,len(Ouro)-1):
  if Ouro[i][1]>Ouro[i+1][1]:
    paises.append(Ouro[i][0]+1)
  else:
    break

for i in range(0,N):
    Prata.append((i,medalhas[i][1]))
ordenarPorMedalhas(Prata)
for i in range(0,len(Prata)-1):
  if Prata[i][1]>Prata[i+1][1]:
    if naoContem(paises,Prata[i][0]+1):
      paises.append(Prata[i][0]+1)
  else:
    break

for i in range(0,N):
    Bronze.append((i,medalhas[i][2]))
ordenarPorMedalhas(Bronze)
for i in range(0,len(Bronze)-1):
  if Bronze[i][1]>Bronze[i+1][1]:
     if naoContem(paises,Bronze[i][0]+1):
      paises.append(Bronze[i][0]+1)
  else:
    break

for i in range(0,N):
  if naoContem(paises,i+1):
    paises.append(i+1)

podio =''
for i in range(0,N):
  podio += str(paises[i])+" "
            
print(podio)