import numpy as np
import pandas as pd

prod_price = [
    [25000, 30000, 15000],
    [10000, 15000, 20000],
    [50000, 30000, 70000]
]
label_name = ['K', "M", "S"]

prod_df = pd.DataFrame(
    prod_price, columns=label_name
)   # 방향주의
print(prod_df)

# 함수 prod_sale = 10% 할인가격으로 변환


def prod_sale(price):
    rst = price * 0.9
    return rst

# print(prod_sale(10000))
# df_k = prod_df[['K', 'M']].apply(prod_sale)
# print(df_k) # df의 컬럼은 = sr과 동일
# prod_df['K_sale'] = df_k
# print(prod_df)

# df_k.columns = ['K_sale', 'M_sale']
# print(df_k)

# prod_df = pd.concat([prod_df, df_k], axis = 1)
# print(prod_df)


# 모든 컬럼에 적용하여 K_sale, M_sale, S_sale을 추가하시오

df_k = prod_df[['K', 'M', 'S']].apply(prod_sale)

df_k.columns = ['K_sale', 'M_sale', 'S_sale']

prod_df = pd.concat([prod_df, df_k], axis=1)
print(prod_df)
