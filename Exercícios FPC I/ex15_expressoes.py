#Exercício - Expressões de Juvenal
#Por se tratar de uma verificação de estruturação entre os parenteses, chaves e colchetes
#a estrutura usada foi a pilha. parenteses, chaves e colchetes abrindo insiro na pilha.
#parenteses, chaves e colchetes fechando e topo correspondente a ele. removo da pilha
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

    def __str__(self):
        s = ''
        i = self._inicio
        while i != None:
            s +='{} |'.format(str(i))
            i = i._prox
        return s

class Pilha(Lista):
    def pop(self):
        return self.removerDoInicio()
  
    def push(self, dado=None):
        novo_no = No(dado)
        if self.isVazia():
            self._fim = novo_no
        else:
            novo_no._prox = self._inicio
            self._inicio._ant = novo_no
        self._inicio = novo_no
  
    def __str__(self):
        return 'Pilha: ' + super().__str__()
  
    def topo(self):
       no = self._inicio
       if not self.isVazia():
           if no._prox == None:
               return str(no)
           else:
               return str(no._prox._ant)
               
    def estaVazia(self):
        return self.isVazia()

t = int(input())
for i in range(0,t):
  A = str(input())
  #separa a string por caracteres sem usar o list()
  A = ' '.join(A).split()
  expressao = Pilha()
  ehValido = 'S'
  for j in A:
    if j == ('(') or j == ('[') or j == ('{'):
          expressao.push(j)
    else:
      if expressao.estaVazia():
        ehValido = 'N'
      else:
        if j == (')') and expressao.topo() == '(':
            expressao.pop()
        elif j == (']') and expressao.topo() == '[':
           expressao.pop()
        elif j == ('}') and expressao.topo() == '{':
            expressao.pop()
        else:
          ehValido = 'N'
        
  if not expressao.estaVazia():
      ehValido = 'N'

  print(ehValido)