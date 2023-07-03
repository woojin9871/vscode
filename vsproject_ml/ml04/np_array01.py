import numpy as np

data = np.array([1, 2, 3, 4, 5])
print([1, 2, 3, 4, 5])
print(data)

# 1차원 슬라이싱
print(data[0:3])    # 인덱스는 0부터 마지막(길이 - 1)

print('====================')

data2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(data2)
print(data2[1, 0:3])