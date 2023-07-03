import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

df = pd.read_csv('./data/fruit_vegetable.csv')
# print(df)
wc = df.set_index('title').to_dict()['count']

# 샘플 사전(dict) 데이터 생성
wcdata = {
        'Today' : 1,
        'we' : 7,
        'have' : 2,
        'learned' : 1,
        'how' : 1,
        'to' : 1,
        'find' : 1,
        'the' : 2,
        'frequency' : 1,
        'of' : 2,
        }
# print(wcdata)
# 워드클라우드로 그리려면 초기화 세팅
wordCloud = WordCloud(
    font_path = 'malgun',
    width = 400,
    height = 400,
    max_font_size = 100,
    background_color = 'white' 
).generate_from_frequencies(wc)

plt.figure()
plt.imshow(wordCloud)
plt.axis('off')
plt.show()


