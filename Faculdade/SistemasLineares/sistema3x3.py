import numpy as np
from scipy import linalg

'''
primeiraEQ = x + y + z = 6
segundaaEQ = x - y + z = 2
terceiraEQ = 2x + y - z = 1

'''

A = np.array([[1,1,1],[1,-1,1],[2,1,-1]])
B = np.array([6,2,1])

solucao = linalg.solve(A, B)
x, y, z = solucao
print(f"Solução: x = {x}, y = {y}, z = {z}")