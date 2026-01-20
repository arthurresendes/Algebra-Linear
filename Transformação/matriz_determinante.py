import numpy as np
from plotagem import plot_vectors

array_1 = [3, 0]
array_2 = [0, 3]

A = np.array([[0.8, 0.3],
              [0.1, 0.7]])

array_1_transformed = np.matmul(A, array_1)
array_2_transformed = np.matmul(A, array_2)
print(array_1_transformed,array_2_transformed)

plot_vectors([array_1, array_2], A)
area = np.linalg.norm(np.cross(array_1, array_2))
print(area)
area_transformed = np.linalg.norm(np.cross(array_1_transformed, array_2_transformed))
print(area_transformed)

det  = np.linalg.det(A)
print(det)

area_deformada  = area * det
area_deformada_transform =  area_transformed * det

print(area_deformada,"\n",area_deformada_transform)