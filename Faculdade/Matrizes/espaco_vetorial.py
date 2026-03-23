import numpy as np

# Criando vetores (elementos do espaço R^n)
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

# Operações básicas
soma = v1 + v2          # Adição vetorial: [5, 7, 9]
escalar = 2 * v1       # Multiplicação por escalar: [2, 4, 6]
produto_p = np.dot(v1, v2) # Produto escalar: 1*4 + 2*5 + 3*6 = 32
