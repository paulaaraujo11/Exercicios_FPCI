def minimo(a,b):
  #retorna o menor entre dois inteiros
  if a < b:
    return a
  else:
    return b

class No(): #Nó de lista duplamente encadeada
  def __init__(self, dado=None):
    self._dado = dado
    self._prox = None
    self._ant = None

  def __str__(self):
    return '{}'.format(self._dado)

class Lista(): #Lista duplamente encadeada
  def __init__(self):
    self._inicio = None
    self._fim = None

  def isVazia(self):
    if self._inicio == None:
      return True
    return False

  def inserirNoFim(self, dado=None):
    novo_no = No(dado)
    if self.isVazia():
      self._inicio = self._fim = novo_no
    else:
      novo_no._ant = self._fim
      self._fim._prox = novo_no
      self._fim = novo_no

  def buscar(self,x):
    i = self._inicio
    while i != None:
      if x == i._dado:
        break
      else:
        i = i._prox
    return i

  def removerElemento(self,x):
    no_encontrado = self.buscar(x)
    if no_encontrado != None:
      if no_encontrado._ant != None:
        no_encontrado._ant._prox = no_encontrado._prox
      else:
        self._inicio = no_encontrado._prox
      if no_encontrado._prox != None:
        no_encontrado._prox._ant = no_encontrado._ant
      else:
        self._fim = no_encontrado._ant
    return no_encontrado

  def removerDoInicio(self):
    no = self._inicio
    if not self.isVazia():
      if no._prox == None:
        self._fim = None
      else:
        no._prox._ant = None
      self._inicio = no._prox

  #função adicionada: contar quantos daquele elemento tem na lista
  def quantos(self,x):
    cont = 0
    i = self._inicio
    while i != None:
      if x == i._dado:
        cont +=1
      i = i._prox
    return cont

  def __str__(self):
    s = ''
    i = self._inicio
    while i != None:
      s +='{} |'.format(str(i))
      i = i._prox
    return s
#===========================================================
N = int(input())
botas_peD = Lista()
botas_peE = Lista()
for i in range(0,N):
  M,L = input().split()
  if L == 'D':
    botas_peD.inserirNoFim(int(M))
  else:
    botas_peE.inserirNoFim(int(M))

peD = peE = par = 0
#o tamanho da bota varia entre 30 e 60.
for i in range(30,61):
  peD += botas_peD.quantos(i)
  peE += botas_peE.quantos(i)
  par += minimo(peE,peD)
  peD = peE = 0
print(par)