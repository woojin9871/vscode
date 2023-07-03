'''
    data/해양수산부_해수욕장_개장일시.csv
    
    추츨조건
            2021년 중에서
            시도별
            해수욕장갯수를 구해서
            막대그래프로 출력하시오
'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import font_manager, rc
font_path ='C:/Windows/Fonts/H2GTRM.TTF'
myfont = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=myfont)

df = pd.read_csv('./data/해양수산부_해수욕장 개폐장일정_20220830.csv')
df_my = df[['	시도', '	해수욕장명', '연도']] 
# print(df_my.shape[0])
df_year = df_my[df_my['연도']==2021]
cities = df_year.groupby('	시도').count()
city_cnt = [len(df_year[df_year['	시도']==city]) for city in cities]

# print(cities)
print(city_cnt)

# x = np.arange(len(cities))
# y =  
# plt.bar(x, y)
# plt.xticks(x, cities)
# plt.show()

