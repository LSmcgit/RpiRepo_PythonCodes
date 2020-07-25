# https://www.youtube.com/watch?v=WQeoO7MI0Bs&t=2703s

import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpeg")
print(img.shape)
width, height = 250, 350
pts1 = np.float32([[164, 27], [240, 57], [111, 146], [187, 181]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("image", img)
cv2.imshow("output", imgOutput)

cv2.waitKey(0)
