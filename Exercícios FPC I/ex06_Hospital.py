#Código  de ordenação Insertion sort retirado do livro "Problem Solving with Algorithms and Data Structures using Python"
#E modificado para a questão
def ordenarPorGrau(arr): 
    for i in range(1, len(arr)): 
        key = int(arr[i][2])
        eKey = arr[i]
        j = i-1
        while j >=0 and key > int(arr[j][2]) : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = eKey
#===================================================

Fila=[]
premium=[]
diamante=[]
ouro=[]
prata=[]
bronze=[]
resto=[]
F = []

n = int(input())

for i in range(0,n):
  nome,plano,grau = [x for x in input().split(" ")]
  Fila.append((nome,plano,grau))
#premium >diamante > ouro > prata > bronze > resto
for i in range(0,n):
  if Fila[i][1] == 'premium':
    premium.append((Fila[i]))
  elif Fila[i][1] == 'diamante':
    diamante.append((Fila[i]))
  elif Fila[i][1] == 'ouro':
    ouro.append((Fila[i]))
  elif Fila[i][1] == 'prata':
    prata.append((Fila[i]))
  elif Fila[i][1] == 'bronze':
    bronze.append((Fila[i]))
  elif Fila[i][1] == 'resto':
    resto.append((Fila[i]))

if len(premium)>=1:
  if len(premium)>1:
    ordenarPorGrau(premium)
    for i in premium:
      F.append((premium[i][0]))
  else:
    F.append((premium[0][0]))

if len(diamante)>=1:
  if len(diamante)>1:
    ordenarPorGrau(diamante)
    for i in diamante:
      F.append((diamante[i][0]))
  else:
      F.append((diamante[0][0]))

if len(ouro)>=1:
  if len(ouro)>1:
    ordenarPorGrau(ouro)
    for i in ouro:
      F.append((ouro[i][0]))
  else:
    F.append((ouro[0][0]))

if len(prata)>=1:
  if len(prata)>1:
    ordenarPorGrau(prata)
    for i in range(0,len(prata)):
      F.append((prata[i][0]))
  else:
    F.append((prata[0][0]))

if len(bronze)>=1:
  if len(bronze)>1:
    ordenarPorGrau(bronze)
    for i in bronze:
      F.append((bronze[i][0]))
  else:
    F.append((bronze[0][0]))

if len(resto)>=1:
  if len(resto)>1:
    ordenarPorGrau(resto)
    for i in range(0,len(resto)):
      F.append((resto[i][0]))
  else:
    F.append((resto[0][0]))

for i in range(len(F)): 
    print (F[i])