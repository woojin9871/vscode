import pandas as pd

S = pd.Series([90, 60, 80, 70])
print(S)

# 160 ~ 190.0 사이 값으로 아무거나 넣어서 출력
S_tall = pd.Series([170.5, 180.1, 166.3, 190.0]) 
print(S_tall)

# 사전 집합 자료와 호환
S_temp = pd.Series([10, 5, 9, 7], index = ['sun','mon','tue','wed']) 
S_hum = pd.Series([12.4, 33.3, 68.2, 45.7], index = ['sun','mon','tue','wed']) 
S_dust = pd.Series({'sun':60, 'mon':30, 'tue':100, 'wed':70})
print(S)
# print(S_temp)
# print(S_hum)
# print(S_dust)

# 길이 얼마?
print(S.size)

# S_prod_list = 상품명 (과일 7개)
S_prod_list = pd.Series(['사과', '배', '바나나', '귤', '수박', '자몽', '복숭아'])
print(S_prod_list)
print(S_prod_list.size)

