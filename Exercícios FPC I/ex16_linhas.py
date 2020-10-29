N = int(input())
#x é uma variável qualquer que ajuda a diminuir o custo. Faz com que o 2° laço não vá até o final
x = 1 
cruzamentos = 0
pregos = [int(i) for i in input().split()]
for i in range(len(pregos)-1,0,-1):
    for j in range(len(pregos)-1-x,-1,-1):
        if pregos[i] < pregos[j]:
          cruzamentos +=1
    x += 1
print(cruzamentos)