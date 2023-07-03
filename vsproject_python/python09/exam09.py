'''
    데이터 형식
                name, math-eng-comp
                김건우, 90-100-80
                윤호민, 80-70-60
                손의성, 100-90-80
                박선호, 80-80-70
                이석호, 90-90-60
                
                열을 분리하고   수학,영어,컴퓨터 합계   평균    분산
'''
import numpy as np
import pandas as pd

data = {'name' : ['김건우', '윤호민', '손의성', '박선호', '이석호'],
        'math_eng_comp' : ['90-100-80', '80-70-60', '100-90-80', '80-80-70', '90-90-60']}

df_da = pd.DataFrame(data)
# print(df_da)

df_da_s = df_da.iloc[:, [1]]
# print(df_da_s)

soc_split = df_da_s.math_eng_comp.str.split('-')
# print(soc_split)

math = soc_split.str.get(0)
eng = soc_split.str.get(1)
comp = soc_split.str.get(2)

df_da['Math'] = math
df_da['Eng'] = eng
df_da['Comp'] = comp

print(df_da[['Math', 'Eng', 'Comp']])
# print(df_da[['Math', 'Eng', 'Comp']])
