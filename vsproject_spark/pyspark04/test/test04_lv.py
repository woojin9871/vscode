import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np
import pandas as pd

font_path = 'C:\Windows\Fonts\H2GTRM.TTF'
my_font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=my_font)

x = np.arange(0.0, 2*np.pi, 0.1)
# print(x)
y = np.sin(x)
# print(y)
plt.plot(x, y)
plt.xlabel('변수x')
plt.ylabel('변수y')
plt.show()