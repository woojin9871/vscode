import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path ='C:/Windows/Fonts/H2GTRM.TTF'
myfont = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=myfont)

df = pd.read_csv('./data/한국교통안전공단_자동차제작결함신고정보_20211231.csv')
# print(df)

df_my = df[['제작사', '접수일자']]

df_my = df_my.dropna()

# print(df_my2.shape[0])
# print(df_my2.count())

# df_sel1 = df_my[df_my['제작사'].str.contains('현대')]
# print(df_sel1)

df_sel1 = df_my[df_my['제작사'].str.contains('현대')]
df_sel2 = df_my[df_my['제작사'].str.contains('기아')]
df_sel3 = df_my[df_my['제작사'].str.contains('쌍용')]
df_sel4 = df_my[df_my['제작사'].str.contains('르노')]
df_sel5 = df_my[df_my['제작사'].str.contains('지엠')]

df_tot = pd.concat([df_sel1, df_sel2, df_sel3, df_sel4, df_sel5])
# print(df_tot)

df_ro = df_tot.groupby('제작사').count().sort_values(by=['접수일자'], axis=0)
print(df_ro)

# ratio = df_ro['접수일자']
# ratio_li = list(ratio)
# print(ratio_li)
# print(type(ratio_li))
ratio = [101, 259, 452, 1679, 2237]
labels = ['쌍용', '지엠', '르노', '기아', '현대']

plt.pie(ratio, labels=labels, autopct='%.1f%%', startangle=90, counterclock=False)
plt.show()

# plt.pie(ratio_li, labels=labels, autopct='%.1f%%', startangle=90, counterclock=False)
# plt.show()
