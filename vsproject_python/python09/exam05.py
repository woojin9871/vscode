'''
    .data/대전, 대구, 제주, 세종, 울산
                상권업종분류명 == '베이커리'
                상호명 = 파리바게트, 뚜레쥬르
'''
import numpy as np
import pandas as pd

df1 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_대전_202212.csv')
df2 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_대구_202212.csv')
df3 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_제주_202212.csv')
df4 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_세종_202212.csv')
df5 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_울산_202212.csv')

df_tot = pd.concat([df1, df2, df3, df4, df5])

# print('대전, 대구, 제주, 세종, 울산 총 수: ', df_tot.shape[0])

dftot_v = df_tot[['상호명', '지점명', '상권업종대분류명', '상권업종중분류명']]
# print(dftot_v)

df_bake = dftot_v[dftot_v['상권업종중분류명']=='제과제빵떡케익']
print('5개 도시 빵집 수 : ', df_bake.shape[0])

# 파리바게트
df_pari = df_bake[df_bake['상호명'].str.contains('리바게')] # 파리바게트, 파리바게뜨, 파리바게트 등 통합
df_pari.index = range(len(df_pari))
print(df_pari.head(n=20))
print('5개 도시 파리바게뜨 수 : ', df_pari.shape[0])

# 뚜레주르
df_tous = df_bake[df_bake['상호명'].str.contains('뚜레쥬르')]
df_tous.index = range(len(df_tous))
print(df_tous.head(n=20))
print('5개 도시 뚜레쥬르 수 : ', df_tous.shape[0])
