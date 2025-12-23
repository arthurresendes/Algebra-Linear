import tensorflow as tf

X = tf.constant([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0]
])

layer = tf.keras.layers.Dense(2)

y = layer(X)

print(y)
