import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np
import pandas as pd

fig = plt.figure()
# 2개의 그래프를 만들겠다
sub1 = fig.add_subplot(2, 1, 1)
sub2 = fig.add_subplot(2, 1, 2)

x = np.arange(0.0, 2*np.pi, 0.1)
y1 = [v*v for v in x]   # 제곱값
y2 = np.sin(x)

sub1.plot(x, y1)
sub2.plot(x, y2)

# 라벨을 추가해보세요 x, y1, y2 이렇게
sub1.set_xlabel('x')
sub1.set_ylabel('y1')

sub2.set_xlabel('x')
sub2.set_ylabel('y2')
plt.show()

