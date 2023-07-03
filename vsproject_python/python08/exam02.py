'''
    넘파이 2차워 배열을 선언하고
    
        수학 점수   영어 점수   과학 점수
            100         80          70
            90          60          70
            90          80          100
            
    데이터 프레임 df 으로 넣으시오
        math    eng     sci
         100     80      70
         90      60      70
         90      80      100
'''
import pandas as pd
import numpy as np

scores = np.array([
    [100, 80, 70],
    [90, 60, 70],
    [90, 80, 100]
])
# print(scores)

df = pd.DataFrame(scores, columns=['math', 'eng', 'sci'])
print(df)