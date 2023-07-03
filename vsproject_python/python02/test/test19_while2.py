# 1~100 까지 while 문으로 합계 구하기
num = 1     # 초기값
sum = 0
while(num <= 100):
    sum += num
    num += 1    # 증가시킴 : 없으면 무한반복
print(sum)
