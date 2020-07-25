# https://www.youtube.com/watch?v=WQeoO7MI0Bs&t=3007

import cv2
import numpy as np

img = cv2.imread("Resources/lena.jpeg")
imgHSV = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
imgHor = np.hstack((img, imgHSV))
imgVer = np.vstack((imgHSV, img))

cv2.imshow("horizontal", imgHor)
cv2.imshow("vertical", imgVer)

cv2.waitKey(0)
cv2.destroyAllWindows()

imgstack = stack