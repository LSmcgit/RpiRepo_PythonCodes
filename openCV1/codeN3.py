import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    cannyImg=cv.Canny(frame,200,200)
    cannyImgResized=cv.resize(cannyImg,(320,240))
    cannyImgCropped=cannyImg[0:200,100:400]

    # Display the resulting frame
    cv.imshow('canny img', cannyImg)
    cv.imshow('resized canny img', cannyImgResized)
    cv.imshow('cropped canny img', cannyImgCropped)

    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()