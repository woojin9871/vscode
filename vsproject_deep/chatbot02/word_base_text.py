import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences


sentences = [
    'I love my dog',
    'I love my cat',
    'You like your cat!',
    'Do you think my dog is cute?'
]

# myToken = Tokenizer(num_words=100)
myToken = Tokenizer(num_words=100, oov_token='<OOV>')   # 토큰화
myToken.fit_on_texts(sentences)
myWord = myToken.word_index
print(myWord)

sentences_other = [
    'I realry love my dog',
    'my dog loves my friend',
    'Do you love your hores?'
]

# sequence = myToken.texts_to_sequences(sentences)
sequence_other = myToken.texts_to_sequences(sentences_other)
# print(sequence)
# print(sentences_other)
pad_seq_other1 = pad_sequences(sequence_other)
pad_seq_other2 = pad_sequences(sequence_other, padding='post')
pad_seq_other3 = pad_sequences(sequence_other, padding='pre', maxlen=6)
pad_seq_other4 = pad_sequences(sequence_other, padding='post', maxlen=6, truncating='post')
print(pad_seq_other1)
print(pad_seq_other2)
print(pad_seq_other3)
print(pad_seq_other4)