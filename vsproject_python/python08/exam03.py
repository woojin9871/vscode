'''
    df  2차원 배열로 정의
        prod_id         prod_name       prod_price
        com-10000       삼성 노트북     1,000,000
        car-10000       엔진 오일          50,000
        com-20000       키보드            100,000
        sport-10000     등산화             80,000
        
    * 판매가는 추가      
'''
import pandas as pd

df = pd.DataFrame({
    'prod_id' : ['com-10000', 'car-10000', 'com-20000', 'sport-10000'],
    'prod_name' : ['삼성 노트북', '엔진 오일', '키보드', '등산화']
})
# print(df)
df['prod_price'] = ['1,000,000', '50,000', '100,000', '80,000']
print(df)

