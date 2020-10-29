#Exercício 13 - Ninguém aguenta mais filas
#Por se tratar de uma fila do dia a dia, a "remoção" pode ser em qualquer ordem (meio, no início ou no fim), diferente da estrutura de dados fila que só pode remover do início. Por isso a estrutura escolhida foi a Lista!
#Classes Nó e Lista foram retiradas da Aula 12
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
      return self._inicio
			self._inicio = no._prox
      

	def __str__(self):
		s = ''
		i = self._inicio
		while i != None:
			s +='{} '.format(str(i))
			i = i._prox
		return s

class Fila(Lista):
	def inserir(self, dado):
		self.inserirNoFim(dado)

	def remover(self):
		return self.removerDoInicio()

	def __str__(self):
		return '' + super().__str__()

F = int(input())
deck_mesa = input().split()

monte_mesa = Fila()
monte_0 = Fila()
monte_1 = Fila()
monte_2 = Fila()

for i in deck_mesa:
  monte_mesa.inserir(i)

_0 = [1,2,1,3]
_1 = [1,7,4]
_2 = [2,3,1]

for i in _0:
  monte_0.inserir(i)

for i in _1:
  monte_1.inserir(i)

for i in _2:
  monte_2.inserir(i)