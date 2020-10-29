def maximo(a,b):
  #retorna o maior entre dois inteiros
  if a > b:
    return a
  else:
    return b

def cortarCanos(n,t,peso,valor):
  # Calcular corte dos canos, usando técnicas de PD 
  # E Problema da mochila
  n +=1
  t +=1
  tabela = [[0 for x in range(t)] for x in range(n)]
  for i in range(0,n):
    for j in range(0,t):
      if i==0 or j==0:
        tabela[i][j] = 0
      elif peso[i-1] > j:
        tabela[i][j] = tabela[i-1][j]
      elif peso[i-1] <= j:
        tabela[i][j] = maximo(valor[i-1] + tabela[i-1][j-peso[i-1]],  tabela[i-1][j])
    
  return tabela[i][j]
#==============================    
n,t = [int(i) for i in input().split()]

peso = []
valor = []
for i in range(0,n):
    p, v = [int(i) for i in input().split()]
    peso.append(p)
    valor.append(v)

print(cortarCanos(n,t,peso,valor))