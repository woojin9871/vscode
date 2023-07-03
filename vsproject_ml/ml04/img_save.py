import numpy as np
import cv2

image_gray = cv2.imread('images/lena.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Gray instead Hangul', image_gray)

cv2.waitKey()

cv2.destroyAllWindows()

cv2.imwrite('output/lena_gray.png', image_gray)     # TRUE