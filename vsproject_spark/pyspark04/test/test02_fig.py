import matplotlib.pyplot as plt

fig = plt.figure()

subplt1 = fig.add_subplot(1, 2, 1) 
subplt2 = fig.add_subplot(1, 2, 2) 
# subplt3 = fig.add_subplot(2, 2, 3) 
# subplt4 = fig.add_subplot(2, 2, 4) 

x = range(1, 100, 2)
y1 = x
y2 = [v ** 2 for v in x]

subplt1.plot(x, y1)
subplt2.bar(x, y2)

plt.show()
