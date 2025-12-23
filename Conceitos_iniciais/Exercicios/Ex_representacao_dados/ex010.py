import numpy as np
import tensorflow as tf

# Relu n deixa negativo
layer = tf.keras.layers.Dense(2, activation='relu')
layer(tf.constant([[0., 0.]]))

w = np.array([[1,-1], [-2,1]])
b = np.array([0,0])

layer.set_weights([w, b])

x = tf.constant([[1.,1.]])

y = layer(x)
print(y)


