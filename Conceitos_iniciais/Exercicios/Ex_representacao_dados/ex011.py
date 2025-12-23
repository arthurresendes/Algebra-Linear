import numpy as np
import tensorflow as tf

layer = tf.keras.layers.Dense(3, activation='relu')
layer(tf.constant([[0., 0.,0.]]))

w = np.array([[1,-1,0], [-2,1,0], [1,1,0]])
b = np.array([0,0,2])

layer.set_weights([w, b])
print(layer.get_weights())
x = tf.constant([[1.,1.,2.]])

y = layer(x)
print(y)


