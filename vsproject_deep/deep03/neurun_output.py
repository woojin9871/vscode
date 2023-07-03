import tensorflow as tf
import numpy as np
from tensorflow import keras

x_train = np.array([[1, 0, 0],[0, 1, 1],[0, 0, 1]])

# 모델을 만들기 전에 뉴런층을 정의
input_layer = tf.keras.layers.InputLayer(input_shape=(3, ))
hidden_layer = tf.keras.layers.Dense(units=4, activation='relu')
output_layer = tf.keras.layers.Dense(units=2, activation='softmax')

model = tf.keras.layers.Sequential([
    input_layer,
    hidden_layer,
    output_layer
])

model.compile(loss='mse', optimizer='Adam')

# hidden layer 가 하나인데 속성값을 출력
hidden_inter1_model = tf.keras.Model()

hidden_output = hidden_inter1_model(x_train)

print('=== 입력 데이터 ===')
print(x_train)

print('=== 중간 hidden 층의 가중치 값 ===')
print(hidden_layer.get_weights()[0])

print('중간 hidden 층의 츨력값')
print(hidden_output)