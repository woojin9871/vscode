'''
    전국 상권 데이터를 모두 읽어서 '상권업종중분류명' 이 '커피점/카페'
    메가커피, 빽다방, 스타벅스 상점의 전국의 각각 총갯수를 각각 구하시오
    https://www.data.go.kr
    소상공인시장진흥공단_상가(상권)정보
'''
import pandas as pd
import numpy as np

df1 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_강원_202212.csv', low_memory=False)
df2 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_경기_202212.csv', low_memory=False)
df3 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_경남_202212.csv', low_memory=False)
df4 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_경북_202212.csv', low_memory=False)
df5 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_광주_202212.csv', low_memory=False)
df6 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_대구_202212.csv', low_memory=False)
df7 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_대전_202212.csv', low_memory=False)
df8 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_부산_202212.csv', low_memory=False)
df9 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_서울_202212.csv', low_memory=False)
df10 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_세종_202212.csv', low_memory=False)
df11 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_울산_202212.csv', low_memory=False)
df12 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_인천_202212.csv', low_memory=False)
df13 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_전남_202212.csv', low_memory=False)
df14 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_전북_202212.csv', low_memory=False)
df15 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_제주_202212.csv', low_memory=False)
df16 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_충남_202212.csv', low_memory=False)
df17 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_충북_202212.csv', low_memory=False)

df_tot = pd.concat([df1, df2, df3, df4, df5, df6, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16, df17])
print(df_tot)

df_my = df_tot[['상호명', '상권업종중분류명']]
# print(df_my)

df_cafe = df_my[df_my['상권업종중분류명']=='커피점/카페']
# print(df_cafe)

df_cafe_me = df_cafe[df_cafe['상호명'].str.contains('메가커피')]
# df_cafe_me.index = range(len(df_cafe_me))
# print(df_cafe_me.head(n=20))
print('전국 메가커피 총 갯수 : ', df_cafe_me.shape[0])

df_cafe_ba = df_cafe[df_cafe['상호명'].str.contains('빽다방')]
# df_cafe_ba.index = range(len(df_cafe_ba))
# print(df_cafe_ba.head(n=20))
print('전국 빽다방 총 갯수' ,df_cafe_ba.shape[0])

df_cafe_st = df_cafe[df_cafe['상호명'].str.contains('스타벅스')]
# df_cafe_st.index = range(len(df_cafe_st))
# print(df_cafe_st.head(n=20))
print('전국 스타벅스 총 갯수' ,df_cafe_st.shape[0])