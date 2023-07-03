import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.arange(5)    # 1 2 3 4 5 (간격 1)
x2 = x + 0.25
y = [90, 80, 90, 60, 70]    # 점수
y2 = [80, 90, 60, 70, 90]    # 점수
name = ['kim', 'oh', 'moon', 'choi', 'john']
# plt.plot
plt.bar(x, y, width=0.25)   #막대길이는 기본 0.8
plt.bar(x2, y2, width=0.25)
plt.xticks(x, name)
plt.xticks(x2, name)
plt.show()