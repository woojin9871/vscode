import pandas as pd

score = pd.Series([90, 60, 50, 70, 40])
# dict 형태이기 때문에 속도 빠름
print(score)
print(score.size)
print(score.sum())