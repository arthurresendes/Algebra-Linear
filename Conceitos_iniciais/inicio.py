import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import pandas as pd
import sentence_transformers
from sentence_transformers import SentenceTransformer
import tensorflow as tf
import torch

'''
print(matplotlib.__version__)
print(np.__version__)
print(pd.__version__)
print(sentence_transformers.__version__)
print(torch.__version__)
print(tf.__version__)
'''

escalar1 = 5
escalar2 = -2
escalar3  = 5**5
escalar4 = 5**(1/2)
escalar5 = np.array(8)
print(escalar5)
print(type(escalar5))
print(escalar5.ndim)

lista = [1,2,3]
print(lista)
print(type(lista))

vector = np.array([1,2,3])
print(vector)
print(type(vector))
print(vector.ndim)

vector *= 2
print(vector)

matriz  = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matriz)
print(matriz.ndim)
print(matriz[0])
print(matriz[1][2])

matriz *= 2
print(matriz)

tensor = np.array(
    [
        [
            [1,2,3],
            [4,5,6] # Lista interna
        ], # Lista intermediaria     
        
        [
            [7,8,9],
            [10,11,12] # Lista interna
        ],  # Lista intermediaria      
    ] # Lista externa
)

print(tensor)
print(tensor.ndim)
tensor *= 2
print(tensor)

tensor_tf = tf.convert_to_tensor(tensor)
print(tensor_tf)
print(type(tensor_tf))

tensor_pt = torch.tensor(tensor)
print(tensor_pt)
print(type(tensor_pt))


print(tensor_tf.numpy())
print(tensor_pt.numpy())