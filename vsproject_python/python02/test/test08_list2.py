L = [1,2,3,4,5,6,7,8,9]
print(L[0:4])
print(len(L))
print(L[4:len(L)])

# 홀수번째 값을 10으로 수정
L[0] = 10
L[2] = 10
L[4] = 10
L[6] = 10
L[8] = 10
print(L)
L.append(10)
print(L)
