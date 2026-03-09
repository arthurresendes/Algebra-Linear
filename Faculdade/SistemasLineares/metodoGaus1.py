import numpy as np

def eliminacao_gaussiana(A, b):
    # Converte para float para evitar erros de divisão inteira
    A = A.astype(float)
    b = b.astype(float)
    n = len(b)
    
    M = np.hstack((A, b.reshape(-1, 1)))
    
    # --- Eliminação Progressiva (Forma Escalonada) ---
    for i in range(n):
        
        max_row = np.argmax(abs(M[i:, i])) + i
        M[[i, max_row]] = M[[max_row, i]]
        
        
        for j in range(i + 1, n):
            fator = M[j, i] / M[i, i]
            M[j, i:] -= fator * M[i, i:]
            
    
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (M[i, -1] - np.dot(M[i, i+1:n], x[i+1:n])) / M[i, i]
        
    return x

# Exemplo:
# 2x + y - z = 8
# -3x - y + 2z = -11
# -2x + y + 2z = -3

A = np.array([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]])
b = np.array([8, -11, -3])

solucao = eliminacao_gaussiana(A, b)
print("Solução (x, y, z):", solucao)

