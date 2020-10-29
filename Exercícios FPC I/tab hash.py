class HashLinearColisao:

     def __init__(self,tam):
          self.tab = {}
          self.tam_max = tam

     def funcaohash(self, chave):
          v = int(chave)
          return (v%int(self.tam_max))

     def cheia(self):
          return len(self.tab) == self.tam_max

     def imprime(self):
          for i in self.tab:
               print("Hash[%d] = " %i, end="")
               print (self.tab[i])

     def apaga(self, chave):
          pos = self.busca(chave)
          if pos != -1:
               del self.tab[pos] 
          else:
            print("Item nao encontrado")

     def busca(self, chave):
          pos = self.funcaohash(chave)
          #essa chave não tem na tabela
          if self.tab.get(pos) == None: 
               return -1
          #retorna chave
          if self.tab[pos] == chave:
               return pos
          else:
            for i in self.tab:
               # se foi inserido apos uma colisão
              if self.tab[i]==chave:
                return i
          return -1

     def insere(self, item):
          if self.cheia():
            print("Error: estouro da tabela hash")
            return
          pos = self.funcaohash(item)
           # se posicao vazia
          if self.tab.get(pos) == None:
               self.tab[pos] = item
           # teve colisão    
          else:
            while True:
              if self.tab[pos] == item: # se o item ja foi cadastrado
                return
              if pos == (self.tam_max - 1):
                pos = -1
                pos = pos + 1
                if self.tab.get(pos) == None:
                  self.tab[pos] = item
                  break
