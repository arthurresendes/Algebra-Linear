import numpy as np
import pandas as pd
from ucimlrepo import fetch_ucirepo
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import sentence_transformers
from sentence_transformers import SentenceTransformer
import tensorflow as tf
import torch

df = pd.DataFrame({
    "número de bebidas": [1, 2, 2, 2],
    "número de entradas": [1, 2, 1, 1],
    "número de pratos principais": [2, 2, 2, 2],
    "número de sobremesas": [2, 1, 1, 1],
    "valor total do couvert": [10, 10, 10, 10],
    "valor da conta": [127.35, 128.10, 134.85, 119.85]
},index=['casal_1','casal_2','casal_3','casal_4'])

df_values = df.values
print(df_values)

x = df_values[:,0:5]
print(x)

y = df_values[:, 5]
print(y)

instacia = df_values[0:1]
print(instacia)
print(instacia.shape)

air_quality = fetch_ucirepo(id=360)

x = air_quality.data.features
print(x)

temperatura = x.loc[:,"CO(GT)":'AH']
print(temperatura)

temperatura_array = temperatura.values
print(temperatura_array)
print(temperatura_array.shape)

temperatura_array_correcao = np.expand_dims(temperatura_array,axis=1)
print(temperatura_array_correcao)

img = mpimg.imread("praia.jpg")

plt.imshow(img)
plt.show()

print(img)

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
sentence = "Let's learn about embeddings!"
embedding = model.encode(sentence)

print(embedding)
print(embedding.shape)

nn = tf.keras.models.Sequential([
    tf.keras.layers.Dense(3, input_shape=[1]),
    tf.keras.layers.Dense(2)
])

print(nn.layers[1].get_weights())
