linha = 3
coluna = 3

matriz = []

for i in range(1,linha+1):
    ex = []
    for j in range(1,coluna+1):
        if i == j:
            res = 0
        else:
            res = i**2 + j**2 
        ex.append(res)
    matriz.append(ex)

print(matriz)