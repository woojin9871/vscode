# 라디안(원주) = 2 * 파이 * 각도 / 360도
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.0, 2*np.pi, 0.1)    # 실수로 증가
y = np.sin(x)
print(y)

plt.plot(x, y)
plt.show()