import numpy as np
import scipy


matriz_ortogonal = np.array([[1/2,-1/2,1/2,-1/2],[1/2,-1/2,1/2,-1/2],[1/2,-1/2,1/2,-1/2],[1/2,-1/2,1/2,-1/2]])

print(np.linalg.norm(matriz_ortogonal,axis=0))
print(np.linalg.norm(matriz_ortogonal,axis=1))
print(np.dot(matriz_ortogonal.T,matriz_ortogonal))
print(np.dot(matriz_ortogonal,matriz_ortogonal.T))