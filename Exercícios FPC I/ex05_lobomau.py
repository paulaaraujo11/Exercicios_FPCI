def percorrerCampo(R, C, campo):
    if campo[R][C] == "#":
        return
    if campo[R][C] == "k":
        global K
        K += 1
    if campo[R][C] == "v":
        global V
        V += 1
    if campo[R][C] != "#":
      campo[R][C] = "#"

    percorrerCampo(R,C+1,campo)
    percorrerCampo(R+1,C,campo)
    percorrerCampo(R-1,C,campo)
    percorrerCampo(R,C-1,campo)

R,C = [int(x) for x in input().split(" ")]
campo = []

#Além das linhas do campo adiciona-se duas linhas verticais(a direita e esquerda) e duas horizontais em cima e embaixo do campo
#Isso ajuda a percorrerr o campo
campo.append(['#']*(C+2))
for x in range(R):
  linhaCampo = list(input())
  linhaCampo.insert(0,'#')
  campo.append(linhaCampo)
  linhaCampo.insert(C+2,'#')
campo.append(['#']*(C+2))
  
ovelha = 0
lobo = 0   
for i in range(1,R+1):
    for j in range(1,C+1):
      K = 0
      V = 0
      percorrerCampo(i,j,campo)
      if K > V:
        ovelha += K
        V = 0
      else:
        lobo += V
        K = 0

print(ovelha , lobo)