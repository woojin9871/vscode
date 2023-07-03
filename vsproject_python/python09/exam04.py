'''
    .data/소상공인시장진흥공단_상가(상권)정보_전남_202212.csv
        상권업종중 분류명 == '도서관'
        전남에 도서관의 갯수가 몇개인가?
'''
import numpy as np
import pandas as pd

df = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_전남_202212.csv')

print('행갯수 ', df.shape[0])

df_my = df[['상호명','상권업종중분류명']]
# print(df_my)

kind = set(df['상권업종중분류명'])
# print(kind)

# 도서관/독서실

df_mystore = df_my[df_my['상권업종중분류명']=='도서관/독서실']

print(df_mystore)
print(df_mystore.shape[0])



