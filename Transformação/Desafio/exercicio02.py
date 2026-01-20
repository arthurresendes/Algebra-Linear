import numpy as np

vetor = np.array([1,0])
graus = 90

res = np.array([
    [np.cos(np.deg2rad(graus)), -np.sin(np.deg2rad(graus))],
    [np.sin(np.deg2rad(graus)),  np.cos(np.deg2rad(graus))]
])

print(res)

det = np.linalg.det(res)
print(det)