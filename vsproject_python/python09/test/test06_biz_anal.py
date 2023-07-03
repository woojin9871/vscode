import numpy as np
import pandas as pd

df1 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_서울_202212.csv')
# 5개 데이터 (서울, 경기, 인천, 부산, 광주)
df2 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_경기_202212.csv')
df3 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_인천_202212.csv')
df4 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_광주_202212.csv')
df5 = pd.read_csv('./data/소상공인시장진흥공단_상가(상권)정보_부산_202212.csv')
# 5개 도시의 데이터 결합

df_tot = pd.concat([df1, df2, df3, df4, df5])

# print('광주 총 수: ', df4.shape[0]) # 78664
# print('부산 총 수: ', df5.shape[0])
print('서울, 경기, 인천, 광주, 부산 총 수: ', df_tot.shape[0])
# print(df1.head(n=5))
print(df1.columns)
dftot_v = df_tot[['상호명', '지점명', '상권업종대분류명', '상권업종중분류명']]
# print(dftot_v)

df_cafe = dftot_v[dftot_v['상권업종중분류명']=='커피점/카페']
print('5 대도시 카페 수 : ', df_cafe.shape[0])

# 이디야
df_cafe_ediya = df_cafe[df_cafe['상호명'].str.contains('이디야')]
df_cafe_ediya.index = range(len(df_cafe_ediya))
print(df_cafe_ediya.head(n=20))
print('5 대도시 이디야 수 : ', df_cafe_ediya.shape[0])

city = list(set(dftot_v['시도명']))
print(city)
# df_test = df_cafe_ediya[df_cafe_ediya['시도명'] == '서울특별시']
# print(df_test.shape[0])
cntpercity = [len(df_cafe_ediya[df_cafe_ediya['시도명'] == A])]
print(cntpercity)
