import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# fig = plt.figure()
# sub = fig.add_subplot(1, 1, 1)
sub_list = plt.subplots(2, 1)  # 2행 1열
sub_list[0][0].plot()
plt.show()