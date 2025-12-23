import numpy as np
import tensorflow as tf

# Quantas saidas de y irá ter, fazendo analogia quantos copos de suco irá ser produzido
layer = tf.keras.layers.Dense(2)

# Definindo quantas engrenagens tera no nosso codigo, como tem 3 x , tem 3 engrenagens
layer(tf.constant([[0., 0.,0.]]))

# 3 engrenagens x 2 dense (resultados), entao o w que são os pesos que iremos trocar pelo layer constrant tem que ser uma matriz 3x2 com 3 linhas e 2 colunas
w = np.array([[2,1],[-1,0],[0,3]])
# len(b) = num dentro do dense
b = np.array([1,-1])

# Passamos o peso e o bais para o layer
layer.set_weights([w, b])

x = tf.constant([[1.,-2.,0.]])

y = layer(x)
print(y)


