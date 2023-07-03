import numpy as np
import pandas as pd

sample = [
    [10, 20, 30],
    [30, 40, 50],
    [50, 60, 70]
]

sum = np.sum(sample)
print(sum)

sum_col = np.sum(sample, axis=0)
print(sum_col)

sum_row = np.sum(sample, axis=1)
print(sum_row)
