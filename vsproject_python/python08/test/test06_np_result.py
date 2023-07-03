import numpy as np

arr_a = np.array([2, 4, 6])
arr_b = np.array([3, 5, 7])
# print(arr_a)
# print(arr_b)
arr_c = arr_a + arr_b
arr_c = np.zeros(3)  # 초기값 0 으로 다시 세팅
# print(arr_c)
# print(arr_c.dtype)

arr2_a = np.array([
    [2, 4, 6],
    [8, 10, 12], 
    [14, 16, 18]
])
arr2_b = np.array([
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
])
# print(arr2_a)
# print(arr2_b)
# print(arr2_a + arr2_b)
arr2_c = arr2_a + arr2_b
arr2_c = np.zeros((3, 3)) 
print(arr2_c)
