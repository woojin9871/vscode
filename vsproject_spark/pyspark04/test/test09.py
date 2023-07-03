import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.arange(5)    # [1, 2, 3, 4, 5]
x2 = x + 0.25
top_y = [1000, 400, 600, 500, 900]  # 제품 갯수
uni_y = [1100, 200, 800, 500, 800]  # 제품 갯수
name = ['cloth', 'shoes', 'cap', 'socks', 'pants']

plt.barh(x, top_y, height=0.2)
plt.barh(x2, uni_y, height=0.2)
plt.yticks(x, name)
plt.yticks(x2, name)
plt.show()

