import pandas as pd

# vsproject_projject 루트폴더임
# data 폴더 생성

df = pd.read_csv('./data/test_file.csv')

# print(df)
# print(df.loc[0])
# print(df.loc[0:1])

print(df.loc[:3, 'LAST_NAME'])  # 행과 열이름 동시에 만족하는 값