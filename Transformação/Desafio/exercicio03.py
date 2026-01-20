import numpy as np

v1 = np.array([2,0])
v2 = np.array([0,3])

area = np.linalg.norm(np.cross(v1, v2))
print(area)

det = 2
area *= det
print(area)

det = -2
area = 6.0 # Trazendo o valor da area base de volta
area *= det
print(area)
