import numpy as np
import tensorflow as tf

layer = tf.keras.layers.Dense(2)
layer(tf.constant([[0., 0.]]))

w = np.array([[1],[1]])
b = np.array([5])

layer.set_weights([w, b])

x = tf.constant([[0.,0.]])

y = layer(x)
print(y)


