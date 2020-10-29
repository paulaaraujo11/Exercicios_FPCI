def buscaNavio(tabuleiro,navios, i, j, pos):
  if tabuleiro[i-1][j] == '#':
    navios[pos].append((i-1, j))
    tabuleiro[i-1][j] = '.'
    buscaNavio(tabuleiro, navios, i-1, j, pos) 
  if tabuleiro[i][j-1] == '#':
    navios[pos].append((i, j-1))
    tabuleiro[i][j-1] = '.'
    buscaNavio(tabuleiro, navios, i, j-1, pos)
  if tabuleiro[i+1][j] == '#':
    navios[pos].append((i+1, j))
    tabuleiro[i+1][j] = '.'
    buscaNavio(tabuleiro, navios, i+1, j, pos)
  if tabuleiro[i][j+1] == '#':
    navios[pos].append((i, j+1))
    tabuleiro[i][j+1] = '.'
    buscaNavio(tabuleiro, navios, i,j+1, pos) 


pos = navios_atingidos = 0
tabuleiro = []
navios = []
disparos = []

N, M = [int(x) for x in input().split(" ")]

#Além das linhas do campo adiciona-se duas linhas verticais(a direita e esquerda) e duas horizontais em cima e embaixo do campo
#Isso ajuda a percorrerr o tabuleiro
tabuleiro.append(['.']*(M+2))
for i in range(1, N+1):
  linhaCampo = list(input())
  tabuleiro.append(['.']+ linhaCampo +['.'])
tabuleiro.append(['.']*(M+2))

#busca os navios existentes no tabuleiro
for i in range(1, len(tabuleiro)):
  for j in range(1, M+1):
    if tabuleiro[i][j] == '#':
      tabuleiro[i][j] = '.'
      navios.append([(i, j)])
      buscaNavio(tabuleiro, navios, i, j, pos) 
      pos+=1
  
K = int(input())

for j in range(K):
  L, C = [int(x) for x in input().split(" ")]
  disparos.append((L, C))

#se o navio for atigindo remove as tuplas com suas coordenadas
for i in range(len(disparos)):
  for j in range(len(navios)):
    if disparos[i] in navios[j]:
      navios[j].remove(disparos[i])

#se for um array vazio ele foi completamente atingido 
for i in navios:
  if i == []:
    navios_atingidos += 1

print(navios_atingidos)