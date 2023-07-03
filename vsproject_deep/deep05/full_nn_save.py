import tensorflow as tf 
import numpy as np
from keras.datasets import mnist
from keras.utils import np_utils

# 데이터를 가져오기 (훈련 데이터 60000, 테스트 데이터 10000)
(x_train, y_train), (x_test, y_test) = mnist.load_data(0)

# 데이터 전처리 0 ~ 1 사이의 값으로 처리
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

# 원 핫 인코딩
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

# 검증 데이터 추출
x_val = x_train[:18000]
y_val = y_train[:18000]
x_train2 = x_train[18000:]
y_train2 = y_train[18000:]

# 모델 구성
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(units=512, activation='relu'),
    tf.keras.layers.Dense(units=10, activation='softmax')
])

# 모델 컴파일
model.compile(loss='categorical_crossentropy',
              optimizer='sgd', metrics=['accuracy'])

# 모델 학습 훈련 (70% 만 사용)
model.fit(x_train2, y_train2, epochs=5, batch_size=32,
          validation_data=(x_val, y_val))

# 모델 평가
loss_and_metrics = model.evaluate(x_test, y_test, batch_size=32)
print('\n', '손실과 정확도' + str(loss_and_metrics))

# 모델 저장
model.summary()
model.save('mnist_mlp_model.h5')