#Função quicksort retirada do pseudocódigo do livro do Cormen: Introduction to Algorithms, 3rd edition.
def funtionQuick(arr):
    def quickSort(lista):
        quickSortHelper(lista,0,len(lista)-1)

    def quickSortHelper(lista,primeiro,ultimo):
      if len(lista) == 1:
        return arr

      if primeiro < ultimo:
        divisor = partition(lista,primeiro,ultimo)
        quickSortHelper(lista,primeiro,divisor-1)
        quickSortHelper(lista,divisor+1,ultimo)

    def partition(lista,primeiro,ultimo):
      i = (primeiro-1)        
      pivo = lista[ultimo]    
      for j in range(primeiro, ultimo):
        if lista[j] <= pivo:
          i = i+1
          lista[i], lista[j] = lista[j], lista[i]
      lista[i+1], lista[ultimo] = lista[ultimo], lista[i+1]
      return (i+1)
	
    quickSort(arr)
    return arr

N,B = [int(i) for i in input().split()]
tam_arquivos = [int(i) for i in input().split()]
i = pastas = 0
j = N-1
#ordena o tamanho dos arquivos em ordem crescente
funtionQuick(tam_arquivos)

while True:
  if (i < j):
    if (tam_arquivos[i] + tam_arquivos[j] <= B):
      i +=1
    j -=1
    pastas +=1
  else:
    break  

if (i == j):
  pastas +=1
print(pastas)