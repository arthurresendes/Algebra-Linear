import numpy as np
import tensorflow as tf

layer = tf.keras.layers.Dense(2, activation='relu')
layer(tf.constant([[0., 0.]]))

w = np.array([[-2,22], [-1,13]])
b = np.array([0,0])

layer.set_weights([w, b])
print(layer.get_weights())
x = tf.constant([[1.,1.]])

y = layer(x)
print(y)


