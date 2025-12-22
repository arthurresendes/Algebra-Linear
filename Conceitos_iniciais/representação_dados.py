import numpy as np
import pandas as pd

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

