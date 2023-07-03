import tensorflow as tf
import numpy as np
from tensorflow import keras
mse_model = keras.Sequential([keras.layers.Dense(units = 3,
                                                 imput_shape = [1])])
 
 # mse 설정
mse_model.compile(loss='mse')   # mean_squared_error 통일 - 약어
# optimzer = 'rmsprop'

xt = [0]
pred = mse_model.predict(xt)
print(pred)
# 0, 1, 0 실제값

mse_model.evaluate(xt, [0, 1, 0])                