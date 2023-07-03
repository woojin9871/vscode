import numpy as np
import pandas as pd

  # 2, 1, 10 행 2, 4, 6 열
  # np arr2 => df
arr2 = np.array([ 
    [2, 4, 6],
    [1, 3, 7],
    [10, 20, 30]
])
print(arr2)

df = pd.DataFrame(arr2, columns=['col1', 'col2', 'col3'])
# print(df)
# df => arr2

df2 = pd.DataFrame({
    'colA' : [2, 4, 6],
    'colB' : [1, 3, 7],
    'colC' : [10, 20, 30]   
})
arr2_result = df2.values
print(arr2_result)

df3 = pd.DataFrame(arr2_result, columns=('col1', 'col2', 'col3'))
print(df3)