import pandas as pd
import numpy as np
from konlpy.tag import Okt
import re

train_data = pd.read_table('data/ratings_train.txt')
test_data = pd.read_table('data/ratings_test.txt')

print(train_data[:5]) # document, label
print(test_data[:5])
print('훈련용데이터 : ', len(train_data)) #150000
print('테스트데이터 : ', len(test_data))

print(train_data['document'].nunique())
train_data.drop_duplicates(subset=['document'], inplace=True)
print('훈련용데이터(중복제거) : ', len(train_data))

#긍정과 부정의 비율
print(train_data.groupby('label').size().reset_index(name='count'))
#널값 유무 및 제거
# print(train_data.isnull().values.any())
# print(train_data.isnull().sum())
# print(train_data.loc[train_data.document.isnull()]) # 25857번
train_data = train_data.dropna(how='any')
print(len(train_data))

# 한글과 공백외에 특수문자 제거
train_data['document']=train_data['document'].str.replace('[^ㄱ-ㅎㅏ-ㅣ가-힣 ]','', regex=True)
# print(train_data[:5])

# 한글과 공백만 남게 되는데 만약 빈데이터가 있으면 널데이터
train_data['document'] = train_data['document'].str.replace('^ +', '', regex=True)
train_data['document'].replace('', np.nan, inplace=True)
# print(train_data.loc[train_data.document.isnull()])
train_data = train_data.dropna(how='any')
print('전처리 후 훈련용 샘플의 개수 : ', len(train_data))

# document 열에서 중복인 내용이 있다면 중복 제거
test_data.drop_duplicates(subset = ['document'], inplace=True) 
# 정규 표현식 수행
test_data['document'] = test_data['document'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","", regex=True) 
# 공백은 empty 값으로 변경
test_data['document'] = test_data['document'].str.replace('^ +', "", regex=True) 
test_data['document'].replace('', np.nan, inplace=True)     # 공백은 Null 값으로 변경
test_data = test_data.dropna(how='any')  # Null 값 제거
print('전처리 후 테스트용 샘플의 개수 : ',len(test_data))

# 2단계 한글문장 토큰화 작업
# 불용어 = 조사 또는 접속사가 대부분
stopword = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']

X_train = []    # train_data에서 토큰화 시킨 단어들
X_test = []
from tqdm import tqdm
from konlpy.tag import Okt
okt = Okt()
for sentence in tqdm(train_data['document']) :
    token_sentence = okt.morphs(sentence, stem=True)    # 토큰화 작업**
    removed_word = [word for word in token_sentence if not word in stopword]
    X_train.append(removed_word)

# print(X_train[:5])

X_test = []
for sentence in tqdm(test_data['document']) :
    token_sentence = okt.morphs(sentence, stem=True) # 토큰화 작업**
    removed_word = [word for word in token_sentence if not word in stopword]
    X_test.append(removed_word)

from keras.preprocessing.text import Tokenizer
tokenizer = Tokenizer()
tokenizer.fit_on_texts(X_train)
print(tokenizer.word_index) # 단어별로 인덱스 출력 (단어:10)

# 단어가 적게 나오는 문장 (2-3개 이하의 문장들) 갯수 조사
threshold = 3   # 문장안에 단어갯수의 최소값
total_cnt = len(tokenizer.word_index) # 총 토큰화 단어 수
rare_cnt = 0    # 단어가 최소 갯수 보다 이하인 문장의 갯수
total_freq = 0  # 훈련데이터의 전체 단어 빈도수 총 합
rare_freq = 0   # 단어 빈도수가 최소값 보다 적게 나오는 문장의 빈도 총 갯수

# 영화 재밌게 봤다
# 영화 보면서 너무 졸려
for key, value in tokenizer.word_counts.items() :   # 단어의 빈수 계산
    total_freq = total_freq + value
    if(value < threshold) :
        rare_cnt = rare_cnt + 1

print('전체 단어 집합의 크기', total_cnt)
print('등장 빈도가 %s번 이하인 희귀 단어 수: %s' %(threshold-1, rare_cnt))
print('단어 집합에서 희귀 단어의 비율 : ', (rare_cnt/total_cnt) * 100)
# print('전체 문자의 단어 빈도수 합 : ', total_freq)

vocab_size = total_cnt - rare_cnt + 1
print("자주 나오는 단어의 집합의 크기 : ", vocab_size)

tokenizer2 = Tokenizer(vocab_size)
tokenizer2.fit_on_texts(X_train)
X_train = tokenizer2.texts_to_sequences(X_train)
X_test = tokenizer2.texts_to_sequences(X_test)    # 테스트 데이터로 검증용

print(X_train[:3])
print(X_test[:3])

# y_train = np.array(train_data['label'])
# y_test = np.array(test_data['label'])
Y_train = np.asarray(train_data['label'])   # 타입처리
Y_test = np.asarray(test_data['label'])


# 시퀀스가 빈 샘플을 찾아서 제거
drop_train = [index for index, setence in enumerate(X_train) if len(sentence) < 1]

X_train = np.delete(X_train, drop_train, axis=0)
Y_train = np.delete(Y_train, drop_train, axis=0)

print(len(X_train))
print(len(Y_train))

# 그래프로 시퀀스의 길이 빈도 대략 20 ~ 30 이하가 대부분 (그래프 생략)
max_length = 30

from keras.utils import pad_sequences

X_train = pad_sequences(X_train, maxlen = max_length)
X_test = pad_sequences(X_test, maxlen = max_length)

# print(X_train[:3])

# Part2 - 딥러닝

import tensorflow as tf
from keras.layers import Embedding, Dense, LSTM
from keras.models import Sequential, load_model
from keras.callbacks import EarlyStopping, ModelCheckpoint

model = Sequential()
model.add(Embedding(vocab_size, 100))   # embedding_dim = 100
model.add(LSTM(128))    # hidden_units = 128
model.add(Dense(1, activation='sigmoid'))

# 훈련하면서 훈련 모델을 저장 : LSTM_best_model.h5
es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=4)
mc = ModelCheckpoint('LSTM_best_model.h5', monitor='val_acc', mode='min', verbose=1, save_best_only=True)

model.compile(loss='binary_crossentropy', optimize='rmsprop', mertrics=['acc'])
model.fit(X_train, Y_train, epochs=15, callback=[es, mc], batch_size=64, validation_split=0.2)
