import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()

iris_data = iris.data
# print(iris_data) 

iris_label = iris.target
# print(iris_label)

iris_feature = iris.feature_names
# print(iris_feature)

iris_df = pd.DataFrame(data=iris_data,
                       columns=iris_feature)

iris_df['label'] = iris_label
# print(iris_df)

X_train, X_test, Y_train, Y_test = train_test_split(iris['data'], iris['target'],
                                                    random_state = 11, test_size=0.3)
print(X_train.shape)
print(X_test.shape)

# 트레이닝 데이터로 학습하기
decision_tree = DecisionTreeClassifier(random_state=40)
decision_tree.fit(X_train, Y_train)

# 랜덤하게 샘플 데이터를 넣어서 예측
X_new = np.array([[7.1, 2.2, 6.8, 0.4]])
prediction = decision_tree.predict(X_new)
# print(prediction)
print('에측결과 : ', iris['target_names'][prediction])

print(decision_tree.score(X_test, Y_test))

# 가지치기 27번 라인으로 가서 max_depth = 3