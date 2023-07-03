import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path ='C:/Windows/Fonts/H2GTRM.TTF'
myfont = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=myfont)

df = pd.read_csv('./data/서울교통공사_역별 일별 시간대별 승하차인원 정보_20221231.csv')
# # print(df)

# df_on =  df[['역명','승하차구분', '06시이전','06-07시간대','07-08시간대','08-09시간대','09-10시간대','10-11시간대','11-12시간대','12-13시간대','13-14시간대','14-15시간대','15-16시간대','16-17시간대','17-18시간대','18-19시간대','19-20시간대','20-21시간대','21-22시간대','22-23시간대','23-24시간대','24시이후']]
# df_fir = df_on[df_on['승하차구분']=='승차']
# df_st = df_fir.groupby('역명').sum()
# df_su = df_st[['06시이전','06-07시간대','07-08시간대','08-09시간대','09-10시간대','10-11시간대','11-12시간대','12-13시간대','13-14시간대','14-15시간대','15-16시간대','16-17시간대','17-18시간대','18-19시간대','19-20시간대','20-21시간대','21-22시간대','22-23시간대','23-24시간대','24시이후']].sum(axis=1)
# sort = df_su.sort_values()

# sort_ta = sort.tail(10)

# x = np.arange(10)
# name = sort_ta('역명')
# # print(name)

# y = sort_ta
# print(sort_ta)
# plt.bar(x, y, width=0.5)   #막대길이는 기본 0.8
# plt.xticks(x, name)
# plt.show()



# 선생님
df_brd = df[df['승하차구분']=='승차']

df_brd = df_brd.loc[:, df_brd.columns != '고유역번호(외부역코드)']
df_brd = df_brd.loc[:, df_brd.columns != '연번']

df_ysum = df_brd.groupby(['호선','역명']).mean() # 상하로 합계
df_avg =pd.DataFrame(df_ysum.sum(axis=1)) # 가로로 합계
df_avg.columns= ['avg']
df_avg2 = df_avg.sort_values('avg', ascending=False)
df_avg3 = df_avg2[0:10]
# print(df_avg2.head(10))

x = np.arange(10)
y = list(df_avg3['avg'])
fig = plt.figure()
sub = fig.add_subplot(1, 1, 1)
sub.bar(x, y)
plt.show()