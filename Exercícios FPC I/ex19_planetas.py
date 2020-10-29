class Hash:
  def _init_(self):
    self.tab = {}
          
  def hash(self, chave):
    return chave%1000

  def busca(self, chave):
    posicao = chave
    if self.tab.get(posicao) == None:
      return -1
    else:
      return posicao

  def insere(self, item):
    posicao = self.hash(item)
    self.tab[posicao] = item
   

pontos = [[0 for i in range(4)] for j in range(10000)] 
regioes = Hash()

M,N = [int(i) for i in input().split()]

for i in range(0,M):
    A,B,C,D = [int(i) for i in input().split()]
    pontos[i][0] = A
    pontos[i][1] = B
    pontos[i][2] = C
    pontos[i][3] = D
  

for i in range(0,N):
    chave = ''
    X,Y,Z = [int(i) for i in input().split()]
    j = 0
    while j < M:
      if( ((pontos[j][0]*X) + (pontos[j][1]*Y) + (pontos[j][2]*Z ) - (pontos[j][3])) > 0 ):
        chave += '1';
      else:
        chave += '0';
      j = j + 1
    
    x = int(str(chave),2)
    temp = regioes.busca(x)
    if (temp != -1):
      regioes.tab[x] = regioes.tab[x] +  1
    else:
      regioes.tab[x] = 1

planetas = 0       
for i in regioes.tab:
  if regioes.tab[i] > planetas:
    planetas = regioes.tab[i]
  
print(planetas)