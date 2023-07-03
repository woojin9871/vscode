score = input('점수를 입력하세요 : ')
score = int(score)

if(score >= 90):
    print('A 입니다')
elif(score >= 80):
    print('B 입니다')
elif(score >= 70):
    print('C 입니다')
elif(score >= 60):
    print('D 입니다')
else:
    print('F 입니다')

# 선생님 버전
if(score >= 90):
    grade = 'A'
elif(score >= 80):
    grade = 'B'
elif(score >= 70):
    grade = 'C'
elif(score >= 60):
    grade = 'D'
else:
    grade = 'F'

print('학점은' + grade + '입니다')
