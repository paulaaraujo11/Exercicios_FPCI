#Lista, Fila e Pilha Python

class No(): #Nó de lista duplamente encadeada
	def __init__(self, dado=None):
		self._dado = dado
		self._prox = None
		self._ant = None

	def __str__(self):
		return 'Dado {}'.format(self._dado)

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

class Fila(Lista):
	def inserir(self, dado):
		self.inserirNoFim(dado)

	def remover(self):
		self.removerDoInicio()

	def __str__(self):
		return 'Fila: ' + super().__str__()


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


if __name__ == '__main__':
	entrada = [4,7,17,89,2,10]
    lista = Lista()
    fila = Fila()
    pilha = Pilha()
    for i in entrada:
    	lista.inserirNoFim(i)
    	fila.inserir(i)
    	pilha.push(i)
    print(lista)
    print(fila)
    print(pilha)