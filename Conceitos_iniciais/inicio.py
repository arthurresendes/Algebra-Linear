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
print(type(vector))