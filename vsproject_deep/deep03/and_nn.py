import tensorflow as tf
import numpy as np
from tensorflow import keras

model_and = keras.Sequential(
    [keras.layers.Dense(units = 3, input_shape=[2]),
     keras.layers.Dense(units=1)]
)

tf.random.set_seed(0)

# 훈련 데이터
x_train = [ [0, 0], [0, 1], [1, 0], [1, 1] ]
y_train = [ [0], [0], [0], [1] ]

# 컴파일
model_and.compile(loss='mse', optimizer='Adam')

result_before = model_and.predict(x_train)
print("훈련 전 예측값 : ", result_before)

# 1000번 훈련
loss_history = model_and.fit(x_train, y_train, epochs = 1000, verbose=1)

result_after = model_and.predict(x_train)
print("훈련한 후 예측값 : ", result_after)

# 손실값의 변화를 그래프로 나타내기
import matplotlib.pyplot as plt

loss = loss_history.history['loss']
plt.plot(loss)
plt.xlabel('count')
plt.ylabel('loss')
plt.show()