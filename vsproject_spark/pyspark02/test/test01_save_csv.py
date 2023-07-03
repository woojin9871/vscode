import pandas as pd
import numpy as np

data = {
    'id' : [1000, 2000, 3000, 4000],
    'name' : ['dev', 'mng', 'sale', 'plan'],
    'location' : [10, 20, 30, 40]
}

# 만일 df가 분석결과라고 하면
df = pd.DataFrame(data)

# csv 저장하려면
# df.to_csv('./data/test_save.csv')

# 인덱스 제거
df.to_csv('./data/test_save.csv', index=False)
