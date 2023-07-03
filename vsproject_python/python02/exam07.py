#튜플 -> 리스트로 변환
T = (1,2,3)
# print(T)
# print(list(T))
L = list(T)
L[0]=0
print(L)

#추가
L.append(4)
print(L)

#삭제
del(L[3])
print(L)