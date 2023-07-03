import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

n_iris = load_iris()

# print(n_iris)   # target = setosa / versicolor / virginica 의 3종류

iris_data = n_iris.data # 컬럼 데이터
# print(iris_data)

iris_label = n_iris.target
# print("타겟 값 : ", iris_label)

# print(n_iris.feature_names) # 컬럼명

df_iris = pd.DataFrame(data=iris_data, columns=n_iris.feature_names)
# 컬럼 추가
df_iris['label'] = iris_label
print(df_iris)