import cv2 as cv
import numpy as np
import time

img=np.zeros((512,512,3),np.uint8)

img[:]= 255,125,0
cv.imshow("image",img)
cv.waitKey(0)

img[:] = 0,0,0
img[100:200,300:310]= 255,125,0
cv.imshow("image",img)
cv.waitKey(0)

img[:]=0,0,0
cv.line(img,(0,0),(300,300),(0,255,255),3)
cv.imshow("image",img)
cv.waitKey(0)

img[:]=0,0,0
cv.line(img,(0,0),(img.shape[0],img.shape[1]),(255,255,255),3)
cv.imshow("image",img)
cv.waitKey(0)

img[:]=0,0,0
cv.rectangle(img,(20,20),(img.shape[0]-20,img.shape[1]-20),(255,0,255),3)
cv.imshow("image",img)
cv.waitKey(0)

cv.rectangle(img,(100,100),(img.shape[0]-100,img.shape[1]-100),(129,0,255),cv.FILLED)
cv.imshow("image",img)
cv.waitKey(0)

img[:]=0,0,0
cv.putText(img,"hello",(256,256),cv.FONT_HERSHEY_SCRIPT_COMPLEX,2,(255,0,255),2)
cv.imshow("image",img)
cv.waitKey(0)
cv.destroyAllWindows()

cap = cv.VideoCapture(0)
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    img=frame
    cv.rectangle(img,(50,50),(img.shape[0]-100,img.shape[0]-100),(0,255,0),2)
    cv.putText(img,"hello",(200,200),cv.FONT_HERSHEY_SCRIPT_COMPLEX,2,(255,255,255),1)

    # Display the resulting frame
    cv.imshow('img', img)

    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()

cv.destroyAllWindows()