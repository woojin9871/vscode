'''
            class   eng     fra     jpn
    data    1       90      70      100
            2       80      60      90
            3       85      80      80
            4       95      70      90
            5       75      90      100
            
    df_score
            데이터프레임을 만든다
         
    apply 메소드와 np.sum 같이 적용해서
            각 반의 합계점수를 구하시오     total_class
            
            각 과목별로 합계점수를 구하시오 total_subject
'''
import numpy as np
import pandas as pd

data = {
    'class' : [1, 2, 3, 4, 5],
    'eng' : [90, 80, 85, 95, 75],
    'fra' : [70, 60, 80, 70, 90],
    'jpn' : [100, 90, 80, 90, 100]
}

df_score = pd.DataFrame(data)
print(df_score)

df_score_class = df_score[['eng', 'fra', 'jpn']]
# print(df_score_class)

total_cl = np.sum(df_score_class, axis=1)
# print(total_cl)

df_score['total'] = total_cl
print(df_score)