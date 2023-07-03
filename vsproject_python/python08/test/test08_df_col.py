import pandas as pd

df = pd.DataFrame({
    'id' : ['kim', 'choi', 'lee', 'sohn', 'song'],
    'passwd' : ['1234', '1111', '2222', '2424', '3322'],
    'name' : ['김건', '최은', '이석', '손흥', '송지']
})
# print(df)
# print(df['id', 'name'])

# 추가
df['age'] = [20, 23, 18, 29, 35]
# df['grnder'] = ['m', 'f', 'm', 'm', 'f']

# df[['age', 'gender']] = [
#     [20, 23, 28, 29, 35],
#     ['m', 'f', 'm', 'm', 'f']
# ]
# print(df)

# 논리값
# df['abult'] = df['age'] >= 19 
# 문자열 숫자 비교해서 추가
df['gubun'] = ['abult' if a >= 19 else 'junior' for a in df['age']]

# 삭제
del df['gubun']
print(df)

