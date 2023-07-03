'''
    10명의 수학점수를 학점을 계산해서 학점별로 학생수를 파이그래츠로 그리기

    점수 90 = A 80 = B ...... 60미만 = F
    grade 컬럼을 만들어서 학점을 저장,
    학점 비율을 파이그래프로 출력하시오
'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

scores = {
    'name' : ['kim', 'oh', 'moon', 'jang', 'choi', 'kim2', 'oh2', 'moon2', 'jang2', 'choi2'],
    'math' : [80, 70, 62, 92, 80, 55, 80, 75, 90, 85]
}
df = pd.DataFrame(scores)
# print(df)
grade = []  # 리스트 변수 정의
df_math = df['math']

for c in df_math:
    if(c >= 90):
        grade.append('A')
    elif(c >= 80):
        grade.append('B')
    elif(c >= 70):
        grade.append('C')
    elif(c >= 60):
        grade.append('D')
    else:
        grade.append('F')

# print(grade)
df['grade'] = grade
# print(df)

ratio = list(df.groupby('grade').count()['math'])
grade_p = ['A', 'B', 'C', 'D', 'F']

plt.pie(ratio, labels=grade_p, autopct='%.1f%%', startangle=90, counterclock=False)
plt.show()
        