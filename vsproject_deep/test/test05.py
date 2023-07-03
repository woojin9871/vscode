import tensorflow as tf
import numpy as np
from tensorflow import keras

tf.random.set_seed(0)

input_layer = tf.keras.layers.InputLayer(input_shape=(3, ))
hidden_layer = tf.keras.layers.Dense(units=4, activation='relu')
output_layer = tf.keras.layers.Dense(units=2, activation='softmax')

model = tf.keras.Sequential([
    input_layer,
    hidden_layer,
    output_layer
])