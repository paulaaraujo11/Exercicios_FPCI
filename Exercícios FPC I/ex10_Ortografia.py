def calcularDistancia(s1, s2):
    m = len(s1)+1
    n = len(s2)+1
    tabelao = [[0 for x in range(n)] for x in range(m)]
    for i in range(1, m):
        tabelao[i][0] = i
    for j in range(1, n):
        tabelao[0][j] = j
        
    for k in range(1, n):
        for l in range(1, m):
            if s1[l-1] == s2[k-1]:
                c = 0
            else:
                c = 1
            tabelao[l][k] = min(tabelao[l-1][k] + 1,    # remoção
                                 tabelao[l][k-1] + 1,   # inserção
                                 tabelao[l-1][k-1] + c) #substituição
    return(tabelao[l][k])
#======================================================================
N, M =  [int(i) for i in input().split()]

p_dicionario = [0 for i in range(N)]
p_analizar = [0 for i in range(M)]

in_dicionario = [[] for i in range(len(p_analizar))]

for i in range(N):
  linha_n = input().lower()
  linha_m = str(linha_n)
  if (len(linha_n)) > 20:
    break
  p_dicionario[i] = linha_n

for j in range(M):
  linha_m = input().lower()
  linha_m = str(linha_m)
  if (len(linha_m)) > 20:
    break
  p_analizar[j] = linha_m

temp = 0
for k in p_analizar:
  for l in p_dicionario:
    k = str(k)
    l = str(l)
    if calcularDistancia(k, l) <= 2:
      in_dicionario[temp].append(l)
  temp +=1

for i in in_dicionario:
  if i == []:
    print('')
  else:
    for j in i:
      print(j, end=" ")
    print('')