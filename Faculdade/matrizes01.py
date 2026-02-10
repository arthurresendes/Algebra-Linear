linha = 3
coluna = 2

matriz = []

for i in range(1,linha+1):
    ex = []
    for j in range(1,coluna+1):
        res = 2 * i - j 
        ex.append(res)
    matriz.append(ex)

print(matriz)