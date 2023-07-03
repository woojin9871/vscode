'''
    .data/codefilex.xls 은행 코드, 지점, 전화번호
                우리은행
                        총 갯수
                        주소를 기준으로 지역별로 갯수
'''
import numpy as np
import pandas as pd

df = pd.read_excel('./data/codefilex.xlsx')
# print(df.head(n=20))
print('전국 은행수 : ', df.shape[0])
# print(df.columns)
print(df['주소'])
