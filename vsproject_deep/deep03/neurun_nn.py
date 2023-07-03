import tensorflow as tf
import numpy as np
from tensorflow import keras

# 랜덤하게 가중치 설정
tf.random.set_seed(0)

# 모델을 만들기 전에 뉴런층을 정의
input_layer = tf.keras.layers.InputLayer(input_shape=(3, ))
hidden_layer = tf.keras.layers.Dense(units=4, activation='relu')
output_layer = tf.keras.layers.Dense(units=2, activation='softmax')

# 모델을 생성
model = tf.keras.Sequential([
    input_layer,
    hidden_layer,
    output_layer
])

# 모델을 컴파일
model.compile(loss='mse', optimizer='Adam')

# 뉴런층속성 : 이름
print('뉴런층 속성 이름')
print(input_layer.name)
print(hidden_layer.name)
print(output_layer.name)

# 입력 rank, 출력 rank
print(input_layer.input)
print(input_layer.output)
print(hidden_layer.input)
print(hidden_layer.output)
print(output_layer.input)
print(output_layer.output)


