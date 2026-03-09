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


A = np.array([[1, 1, 1], [0, 2, 5], [2, 5, -1]])
b = np.array([6, -4, -27])

solucao = eliminacao_gaussiana(A, b)
print("Solução (x, y, z):", solucao)

