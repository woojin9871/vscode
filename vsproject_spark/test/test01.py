import pandas as pd
import numpy as np
import glob as glob # 디렉토리 접근 모듈 

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

# csvfiles = glob.glob('./data/smal_biz/*.csv')
# print(len(csvfiles))    # 리스트 목록

# for file in csvfiles:
#     df_temp = pd.read_csv(file, low_memory=False) 
#     df_tot=  pd.concat([df_tot, df_temp])

df_tot = pd.concat([df1, df2, df3, df4, df5, df6, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16, df17])
# print(df_tot)

df_my = df_tot[['상호명', '상권업종중분류명']]
# print(df_my)

df_con = df_my[df_my['상권업종중분류명']=='종합소매점']
# print(df_con)

df_con_gs = df_con[df_con['상호명'].str.contains('GS25')]
print('전국 GS25 총 갯수 : ', df_con_gs.shape[0])

df_con_cu = df_con[df_con['상호명'].str.contains('CU')]
print('전국 CU 총 갯수' ,df_con_cu.shape[0])

df_con_sev = df_con[df_con['상호명'].str.contains('세븐일레븐')]
print('전국 세븐일레븐 총 갯수' ,df_con_sev.shape[0])