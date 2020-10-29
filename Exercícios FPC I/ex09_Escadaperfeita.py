#escadas rolantes em python - Ex09

totalBlocos = 0
movimentos = 0
temp = 0

n = int(input())
pilhas = list(map(int, input().split()))

for i in range(0,n):
    totalBlocos += pilhas[i]

b = (((2*totalBlocos)/n)+(n-1))//2
a = 1+b-n

for i in range(0,n):
    temp +=(pilhas[i]-(i+a))
    if (pilhas[i]>i+a):
        movimentos+=(pilhas[i]-(i+a));

if (temp != 0):
    print('-1')
else:
    print(movimentos)