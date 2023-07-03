# 학생들의 키
# TALL 170.5, 180.6, 174.3
# 평균키를 구하시오

tall = [170.5, 180.6, 174.3]
sum = 0
for a in tall:
    sum = sum + a / len(tall)
print(sum)
    
print()
    
# 선생님 버전
TALL = [170.5, 180.6, 174.3]
sum_tall = 0
for t in TALL:
    sum_tall = sum_tall + t
count = len(TALL)
avreage = sum_tall / count
print(avreage)
