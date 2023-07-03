import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [1, 2, 3, 4, 5]
y1 = [2, 3, 4, 5, 6]
y2 = [1, 4, 9, 16, 25]

plt.plot(x, y1, label='Price(won)')
plt.plot(x, y2, label='Demand(cnt)')
plt.legend(ncol=2)
plt.show()