import numpy as np
import tensorflow as tf
import torch


escalar = 5**(1/2)
escalar1 = np.array(8)
print(escalar1)
print(type(escalar1))
print("Numero escalar ndim: ")
print(escalar1.ndim)


vetor = np.array([0,10,20,30,40,50])
print(vetor)
print(type(vetor))
print("Numero vetor ndim: ")
print(vetor.ndim)

matriz = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(matriz)
print(type(matriz))
print("Numero matriz ndim: ")
print(matriz.ndim)
matriz *= 2
print(matriz)


tensor_np = np.array([
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [1,2,3],
        [4,5,6]
    ],
])

print(tensor_np)
print(type(tensor_np))
print("Numero tensor ndim: ")
print(tensor_np.ndim)
tensor_np *= 2
print(tensor_np)

tensor_tf = tf.convert_to_tensor(tensor_np)
print(tensor_tf)
print(type(tensor_tf))

tensor_th = torch.tensor(tensor_np)
print(tensor_th)
print(type(tensor_th))