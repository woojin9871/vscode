'''
    iris data 데이터에서
    apply & count_missing 함수를 사용해서
    결측값이 몇개 있는지 체크

    sepal 길이 컬럼만 번올림해서 sepal_new 컬럼으로 추가
'''

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris


n_iris = load_iris()

iris_data = n_iris.data
# print(iris_data)

iris_label = n_iris.target
# print(iris_label)

df_iris = pd.DataFrame(data=iris_data, columns=n_iris.feature_names)
# print(df_iris)


def count_missing(vec):
    null_vec = pd.isnull(vec)
    count_null = np.sum(null_vec)
    return count_null


df_miss = df_iris.apply(count_missing)
# print(df_miss)


def func(input):
    out = round(input)
    return out


df_se = df_iris['sepal length (cm)']
print(df_se)
