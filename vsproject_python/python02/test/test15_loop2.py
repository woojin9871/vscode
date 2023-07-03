# score = 90, 80, 95
# 총합을 구하시오 sum 에 저장 출력

# 반복문 미사용
score = [90, 80, 95]
sum = 0     # 초기값 
sum = sum + score[0]
sum = sum + score[1]
sum = sum + score[2]
print(sum)

# 반복문 사용
sum2 = 0
for s in score:
    sum2 = sum2 + s
print(sum2)
    
    


