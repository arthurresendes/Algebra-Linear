import numpy as np

vetor_a = np.array([[1, 1, 1, 2, 2],
              [1, 2, 2, 2, 1],
              [1, 2, 1, 2, 2],
              [1, 2, 1, 2, 1]])

vetor_y =  np.array([127.35, 128.10, 134.85, 119.85])

a_inv = np.linalg.pinv(vetor_a)
x = np.dot(a_inv,vetor_y)

print(x)

y = np.dot(vetor_a, x)
print(y)


vetor_a = np.array([[1, 1, 1, 2, 2],
              [1, 2, 2, 2, 1],
              [1, 2, 1, 2, 2],
              [1, 2, 1, 2, 1],
              [1, 2, 2, 1, 1]])

vetor_y = np.array([127.35, 128.10, 134.85, 119.85, 92.3])

a_inv = np.linalg.pinv(vetor_a)
x = np.dot(a_inv, vetor_y)
print(x)