import tensorflow as tf
import numpy as np
from tensorflow import keras

model = keras.Sequential([keras.layers.Dense(units=3, input_shape=[1])])
model2 = tf.keras.models.clone_model(model)

model.compile(loss='mean_squared_error', optimizer='Adam')
model2.compile(loss='mean_squared_error', optimizer='RMSprop')

model.evaluate([0], [[0, 1, 0]])
model2.evaluate([0], [[0, 1, 0]])
