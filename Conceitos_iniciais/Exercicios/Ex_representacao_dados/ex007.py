import numpy as np
import tensorflow as tf

layer = tf.keras.layers.Dense(2) # Da 2 saidas de result
layer(tf.constant([[0., 0., 0.]]))

w = np.array([[2,1],[-1,0],[0,3]])
b = np.array([1,-1])

layer.set_weights([w, b])

x = tf.constant([[1.,-2.,0.]])
y = layer(x)
print(y)



