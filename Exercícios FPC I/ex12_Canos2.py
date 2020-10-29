def maximo(a,b):
  #retorna o maior entre dois inteiros
  if a > b:
    return a
  else:
    return b

def cortarCanosAtualizado(n,t):
  # add mais um espaço a lista para ter a parada/ponto de inicio
  # E pq tbm tenho lucro zero sem vender nada
  list_lucros = [0 for x in range(t+1)] 
  for i in range(0,t+1):
    for j in range(0,n):
      if(comprimento[j] <= i):
        list_lucros[i] = max(list_lucros[i - comprimento[j]] + valor[j],list_lucros[i]);
        
  return(list_lucros[t])

#====================================================================   
n,t = [int(i) for i in input().split()]

comprimento = []
valor = []
for i in range(0,n):
    p, v = [int(i) for i in input().split()]
    comprimento.append(p)
    valor.append(v)