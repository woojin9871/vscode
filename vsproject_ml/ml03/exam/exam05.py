'''
    ./data/titanic.csv
    Survived    성별    나이    기타등등
    1
    2
    ...
    10
    (누락값 제외)       10개 행만 뽑아서
            성별
                    남자                    여자
                    Age >= 30   Age < 30    Age >= 30   Age < 30
                    
            생존확률?
                            1           2           5           2
'''
import pandas as pd
import numpy as np

df = pd.read_csv('./data/titanic.csv')
# print(df.head(n=10))
df_life = df[['Survived', 'Sex', 'Age']]
# print(df_life.head(n=10))

df_life = df_life.dropna()
df_life_10 = df_life.head(n=10)       # 5번째 결측데이터는 제거
print(df_life_10)

print(df_life_10)
total = df_life_10.shape[0]
print('전체 행 갯수', total)

print('생존자 수는 : ', df_life_10['Survived'].sum(axis=0))     # 0 기본값 - 상하

count_m = 0
count_m2 = 0
count_f = 0
count_f2 = 0
def cal_survived(vec):
        # count = 0       # 로컬 변수
        global count_m
        global count_m2
        global count_f
        global count_f2
        if(vec[0] == 1 and vec[1] == 'male'):
                if(vec[2] <= 30):
                        count_m = count_m + 1
                else:
                        count_m2 + count_m2 + 1                
        elif(vec[0] == 1 and vec[1] == 'female'):
                if(vec[2] >= 30):
                        count_f = count_f + 1
                else:
                        count_f2 = count_f2 + 1
                        
# print(cal_survived(1))
df_life_10[['Survived', 'Sex', 'Age']].apply(cal_survived, axis=1)
print('남자 생존자 수는(30 이상) : ', count_m, '확률 : ', count_m/total)
print('남자 생존자 수는(30 이하) : ', count_m, '확률 : ', count_m2/total)
print('여자 생존자 수는(30 이상) : ', count_f, '확률 : ', count_f/total)
print('여자 생존자 수는(30 이하) : ', count_f2, '확률 : ', count_f2/total)