import numpy as np
import cv2

fname = 'images/lena.jpg'

image_color = cv2.imread(fname, cv2.IMREAD_COLOR)   # 컬러는 기본값

cv2.imshow('color instead hangule', image_color)

cv2.waitKey()

cv2.destroyAllWindows()