'''
    'name' : ['kim', 'choi', 'yoon'],
    'math' : ['90', '80', '70'],
    'kor' : ['100', '90', '90']

    각 사람의 성적합계를 구하고
    name, math, kor, tot 이렇게 컬럼으로 저장
    score_num.csv
'''
import pandas as pd
import numpy as np

data = {
    'name' : ['kim', 'choi', 'yoon'],
    'math' : [90, 80, 70],
    'kor' : [100, 90, 90],  
    'tot' : [0, 0, 0]
}

# 열값 추가
df = pd.DataFrame(data)
df['tot'] = df[['math', 'kor']].sum(axis=1)

# 행값 추가
df2 = df

df2.loc[3] = [np.NaN, df['math'].sum() ,df['kor'].sum(), np.NaN]
print(df2)

# print(df)

df.to_csv('./data/socre_sum.csv', index=False)