import numpy as np
import tensorflow as tf

layer = tf.keras.layers.Dense(1)
layer(tf.constant([[0., 0.]]))

w = np.array([[3],[3]])
b = np.array([2])

layer.set_weights([w, b])

x = tf.constant([[4.,0.]])

y = layer(x)
print(y)


