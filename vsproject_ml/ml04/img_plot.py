import numpy as np
import cv2
from matplotlib import pyplot as plt 

fname = 'images/lena.jpg'

image_color = cv2.imread(fname, cv2.IMREAD_COLOR)

plt.imshow(image_color)
plt.xticks([])
plt.xticks([])
plt.show()