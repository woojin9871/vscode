import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import font_manager, rc
font_path ='C:/Windows/Fonts/H2GTRM.TTF'
myfont = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=myfont)

# csv 파일 리딩
df1 = pd.read_csv('./data/small_biz/소상공인시장진흥공단_상가(상권)정보_서울_202212.csv')
df2 = pd.read_csv('./data/small_biz/소상공인시장진흥공단_상가(상권)정보_경기_202212.csv')
df3 = pd.read_csv('./data/small_biz/소상공인시장진흥공단_상가(상권)정보_인천_202212.csv')
df4 = pd.read_csv('./data/small_biz/소상공인시장진흥공단_상가(상권)정보_부산_202212.csv')
df5 = pd.read_csv('./data/small_biz/소상공인시장진흥공단_상가(상권)정보_광주_202212.csv')
df_tot = pd.concat([df1, df2, df3, df4, df5])
# print(df_tot.shape[0])

cities = ['서울특별시', '인천광역시', '경기도', '광주광역시', '부산광역시']

df_tot_cafe = df_tot[df_tot['상권업종중분류명']=='커피점/카페']
# print(df_tot_cafe.shape[0])

cities = ['서울특별시','인천광역시','경기도','광주광역시', '부산광역시']
dfv = df_tot_cafe[['상호명','상권업종대분류명','상권업종중분류명','시도명']]
dfv_paikcoff = dfv[dfv['상호명'].str.contains('빽다방')]
# dfv_5city = df_tot[df_tot['시도명']==city] 
city_cnt = [len(dfv_paikcoff[dfv_paikcoff['시도명']==city]) for city in cities]
print(city_cnt)

x = np.arange(len(cities))
y = city_cnt
plt.bar(x, y)
plt.xticks(x, cities)
plt.show()