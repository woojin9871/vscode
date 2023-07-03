import numpy as np

LST = [1, 3, 5, 7, 9]
arr = np.array(LST)
# print(arr)
# print(arr.shape)    # (5, 열)

arr2 = np.array([LST, LST, LST, LST, LST])
# print(arr2)
# print(arr2.shape)
print(arr2.dtype)

# 파이썬 문법처럼 배열의 값을 이미 알고 있다
a = 1
b = 2
c = a+b
print(c)