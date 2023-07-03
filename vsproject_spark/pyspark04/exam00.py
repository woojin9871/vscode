'''
    figure 사용해서 그래프를 두 개 만들고
    sin 그래프 를 그리고
    cosine 그래프를 그리시오
'''
import matplotlib.pyplot as plt 
import numpy as np

fig = plt.figure()

sub1 = fig.add_subplot(1, 2, 1)
sub2 = fig.add_subplot(1, 2, 2)

x1 = np.arange(0.0, 2*np.pi, 0.1)
y1 = np.sin(x1)

x2 = np.arange(0.0, 2*np.pi, 0.1)
y2 = np.cos(x2)

sub1.plot(x1, y1)
sub2.plot(x2, y2)
plt.show()


