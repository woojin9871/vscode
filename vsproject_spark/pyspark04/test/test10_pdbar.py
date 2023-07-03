import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

scores = {
    'name' : ['kim', 'oh', 'moon', 'choi', 'john'],
    'math' : [90, 80, 90, 60, 70],
    'eng' : [70, 70, 60, 90, 80],
    'com' : [80, 80, 80, 80, 90]
} 
df = pd.DataFrame(scores)   # 결과값
df.index = range(len(df))
# print(df)

# 각 사람의 총합, 평균 구해서 막대 그래프를 그리시오
plt.title('학생명 평균')
summation = list(df[['math', 'eng', 'com']].sum(axis=1))
average = list(df[['math', 'eng', 'com']].mean(axis=1))
# print(summation)

x = np.arange(len(df))    # 행의 길이 범위를 사용함
x2 = x + 0.3
# y = list(df['math'])
y = summation
y2 = average
name = list(df['name'])

fig = plt.figure()
sub1 = fig.add_subplot(1, 1, 1)
sub1.bar(x, y, width=0.3)
sub1.bar(x2, y2, width=0.3)
sub1.set_xticks(x, name)
plt.show()