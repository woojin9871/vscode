# for 반복문을 사용하여 ,
# 1에서 100까지 짝수의 합과 홀수의 합을 각각 출력하시오
# 반복문 + 조건문 같이 사용

sum_all = 0
sum_even = 0
sum_odd = 0

for n in range(1,101):
    # sum_all = sum_all + n
    if(n % 2 == 0):
        sum_even = sum_even + n
    else:
        sum_odd = sum_odd + n

print(sum_even)
print(sum_odd)






