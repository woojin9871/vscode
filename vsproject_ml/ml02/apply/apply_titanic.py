import numpy as np
import pandas as pd

# 1번
df_t = pd.read_csv('./data/titanic.csv')
print(df_t.head(n=5))

# pd.isnull 누락값 여부 체크


def check_missing(vec):
    null_vec = pd.isnull(vec)
    return null_vec

# 컬럼별로 누락값의 갯수


def count_missing(vec):
    null_vec = pd.isnull(vec)
    count_null = np.sum(null_vec)
    return count_null

# 각 컬럼이 누락의 비율


def prop_missing(vec):
    total = count_missing(vec)  # 누락 총 개
    rowlen = vec.size
    rst = total / rowlen    # 1 - (total / rowlen)
    return rst


rowlen_test = df_t.shape[0]
print('행의 총 개수 : ', rowlen_test)

total_test = np.sum(np.isnull(df_t['Embarked']))
print(total_test)

df_cnt_m = df_t.apply(count_missing, axis=1)    # 한 행에대해 여러개 열에 적용
# print(df_cnt_m)

# vx = np.NaN
# vx2 = 10000
# rst = check_missing(vx)
# print(rst)
# rst2 = check_missing(vx2)
# print(rst2)

# df_miss = df_t.isna()
# print(df_miss)

df_miss = df_t.apply(count_missing)
# print(df_miss)

df_prop_m = df_t.apply(prop_missing)
# print(df_prop_m)

df_t['num_missing'] = df_t.apply(count_missing, axis=1)
# print(df_t.head(n=5))

df_t_final = df_t.loc[df_t.num_missing > 1, :]
print(df_t_final.head(n=5))
