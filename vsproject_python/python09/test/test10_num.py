import pandas as pd
import numpy as np
import glob as  glob

Lmath = ['100', '90', 70]
sr = pd.Series(Lmath)

# print(pd.to_numeric(sr, errors='coerce'))
# print(pd.to_numeric(sr).sum())

data = {
    'name' : ['김김', '소소', '노노'],
    'eng' : ['80', 90, 'missing']
}
df_class = pd.DataFrame(data)
# 영어 점수의 총합을 구하시오

# print(pd.to_numeric(df_class['eng'], errors='coerce'))
# print(pd.to_numeric(df_class['eng'], errors='coerce').sum()) # NaN 행은 제외하고

data2 = {
    'name' : ['김김', '소소', '노노'],
    'eng' : ['80', 90, '70'],
    'math' : ['70', 80, '90']
}
df_class2 = pd.DataFrame(data2)
# print(df_class2)
# 각 사람의 총합을 'total' 컬럼으로 구하시오

df_class2['eng'] = pd.to_numeric(df_class2['eng'])
df_class2['math'] = pd.to_numeric(df_class2['math'])

print(df_class2)
# print(df_class2[['eng','math']].sum(axis=1))
df_class2['total'] = df_class2[['eng','math']].sum(axis=1)
print(df_class2)

