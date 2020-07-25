import cv2
import numpy as np
cap = cv2.VideoCapture(0)
ret, img = cap.read()
#img=cv2.imread("Resources/lambo.png")
if not ret:
    print("Can't receive frame (stream end?). Exiting ...")

cv2.imshow("regular img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("gaussian blur",cv2.GaussianBlur(img,(21,21),0))
cv2.waitKey(0)

cv2.imshow("cv2.COLOR_BGR2GRAY",cv2.cvtColor(img,cv2.COLOR_BGR2GRAY))
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("cv2.COLOR_BAYER_GB2BGR_VNG",cv2.cvtColor(img,cv2.COLOR_BGR2LAB))
cv2.waitKey(0)
cv2.destroyAllWindows()

#image dialation
cv2.imshow("cv2.Canny",cv2.Canny(img,200,200))
cv2.waitKey(0)
cv2.destroyAllWindows()
imgCanny=cv2.Canny(img,200,200)
kernel=np.ones((5,5),np.uint8)
cv2.imshow("dilation kernel",cv2.dilate(imgCanny,kernel,iterations=3))
cv2.waitKey(0)
cv2.destroyAllWindows()

#image erotion
imgDilated=cv2.dilate(imgCanny,kernel,iterations=3)
imgEroded=cv2.erode(imgDilated,kernel,iterations=2)
cv2.imshow("eroded image", imgEroded)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.waitKey(0)
cv2.destroyAllWindows()