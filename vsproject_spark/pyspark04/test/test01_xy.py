import matplotlib.pyplot as plt 

x = range(0, 10)

y1 = [v*v for v in x]
y2 = (x)
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()