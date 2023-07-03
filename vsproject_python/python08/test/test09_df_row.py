import pandas as pd

df = pd.DataFrame({
    'id' : ['kim', 'choi', 'lee', 'sohn', 'song'],
    'passwd' : ['1234', '1111', '2222', '2424', '3322'],
    'name' : ['김건', '최은', '이석', '손흥', '송지']
})

# print(df[0:3])      # 슬라이싱 마지막 번호 크기 - 1
# print(df.loc[0:2])  # 마지막 번호 = 크기(인덱스) 
# print(df.loc[:0, 'id'])
df.loc[5,:] = ['park', '3333', '박대']  # 6번째
# df.drop(df.index[5], axis=0, inplace=True)    # 인덱스 5번 삭제
df.drop(df.index[4, 5], axis=0, inplace=True)    # 인덱스 4-5번 (6번)
print(df)