def maximo(a,b):
  #retorna o maior entre dois inteiros
  if a > b:
    return a
  else:
    return b

def cortarCanosAtualizado(i,t):
  if i == n:
    return 0

  elif t == 0:
    return 0

  elif t < 0:
    return -1

  ans = matriz[i][t]

  if ans == -1:
    ans = maximo(cortarCanosAtualizado(i + 1, t), valor[i] + cortarCanosAtualizado(i, t - peso[i]));
    print(ans)
  return ans;
  
#==============================    
n,t = [int(i) for i in input().split()]

peso = []
valor = []
for i in range(0,n):
    p, v = [int(i) for i in input().split()]
    peso.append(p)
    valor.append(v)

matriz = []

matriz = [[-1 for x in range(t+1)] for x in range(n+1)]


print(cortarCanosAtualizado(0, t))