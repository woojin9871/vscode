import pandas as pd

# s = pd. Series({0 : 1, 1 : 10})
# print(s)
df = pd.DataFrame(
    {
        'A_col' : 1.0,
        'B_col' : [1, 2, 3, 4, 5],                   
    }
)
print(df)
print(df.index)
print(df.columns)