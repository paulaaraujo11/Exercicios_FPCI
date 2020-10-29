#O elevador é ativado cada vez que passa uma pessoa, e dura 10 seg
#quanto tempo elevador fica ativo? 

#se a diferença entre os momentos é maior que 10, adiciono somente a diferença,
#se não somo a difernça ao tempo total. Ao final de tudo somo mais 10 seg(a referente a última pessoa)
momentos = []
tempo = difTempo = 0
n_pessoas = int(input())
for i in range(n_pessoas):
  momentos.append(int(input()))

for i in range(n_pessoas-1,0,-1):
  difTempo = momentos[i] - momentos[(i-1)]
  if (difTempo > 10):
  	tempo += 10
  else:
  	tempo += difTempo
tempo += 10
print(tempo)