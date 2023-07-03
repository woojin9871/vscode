import json

with open('data/sarcasm.json', 'r') as f:
    datastore = json.load(f)
    
sentences = []
labels = []
urls = []

for item in datastore:
    sentences.append(item['headline'])
    labels.append(item['is_sarcastic'])
    urls.append(item['article_link'])

# print(sentences)
# print(labels)
# print(urls)

# 2단계 - 영어 자연어 처리
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences

news_token = Tokenizer(oov_token="<OOV>")
news_token.fit_on_texts(sentences)

news_words = news_token.word_index
print(news_words)
print(len(news_words))

my_sentence = [
    'we want to study computer and java, we will go to USA next year'
]
news_seq = news_token.texts_to_sequences(my_sentence)
print(news_seq)
# print(len(news_seq))
news_paddeds = pad_sequences(news_seq)
print(news_paddeds[0])