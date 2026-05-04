import numpy as np

def pertence_subespaco(v):
    return np.isclose(v[2], v[0] + v[1])

v1 = np.array([1, 2, 3])
v2 = np.array([1, 2, 4])

print(f"v1 pertence: {pertence_subespaco(v1)}")
print(f"v2 pertence: {pertence_subespaco(v2)}")