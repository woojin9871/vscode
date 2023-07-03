import tensorflow as tf
import numpy as np
from tensorflow import keras

model = keras.Sequential([keras.layers.Dense(units=1, 
                                                    input_shape=[1])])

model.compile(loss='mean_squared_error', optimizer='sgd')