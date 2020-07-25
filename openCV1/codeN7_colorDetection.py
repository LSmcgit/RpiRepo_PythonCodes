# https://www.youtube.com/watch?v=WQeoO7MI0Bs&t=3378

import cv2
import numpy as np
import time


def empty(a):
    pass


def scale_pic(image, scale_percent):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    img_resized = cv2.resize(img, dim)
    return img_resized


path = 'Resources/lambo.jpg'

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

cv2.namedWindow("trackBars")
cv2.resizeWindow("trackBars", 640, 240)

# hsv values
cv2.createTrackbar("hue min", "trackBars", 0, 179, empty)
cv2.createTrackbar("hue max", "trackBars", 179, 179, empty)
cv2.createTrackbar("sat min", "trackBars", 0, 255, empty)
cv2.createTrackbar("sat max", "trackBars", 255, 255, empty)
cv2.createTrackbar("val min", "trackBars", 0, 255, empty)
cv2.createTrackbar("val max", "trackBars", 255, 255, empty)


while True:
    # Capture frame-by-frame
    ret, img = cap.read()
    # img = cv2.GaussianBlur(img, (21, 21), 0)
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # img = cv2.imread(path)
    # img = scale_pic(img, 35)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    h_min = cv2.getTrackbarPos("hue min", "trackBars")
    h_max = cv2.getTrackbarPos("hue max", "trackBars")
    s_min = cv2.getTrackbarPos("sat min", "trackBars")
    s_max = cv2.getTrackbarPos("sat max", "trackBars")
    v_min = cv2.getTrackbarPos("val min", "trackBars")
    v_max = cv2.getTrackbarPos("val max", "trackBars")

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)

    imgResult = cv2.bitwise_and(img, img, mask=mask)
    # cv2.imshow("original", img)
    # cv2.imshow("HSV", imgHSV)
    # cv2.imshow("mask", mask)
    # cv2.imshow("result", imgResult)
    cv2.imshow("stacked", np.hstack((img, imgResult)))
    # print(h_min, h_max, s_min, s_max, v_min, v_max)

    cv2.waitKey(1)





