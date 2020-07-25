# https://youtu.be/WQeoO7MI0Bs?t=6034

import cv2
import numpy

def scale_pic(image, scale_percent):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    img_resized = cv2.resize(img, dim)
    return img_resized

def findFace(img, faces):

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        facePosition = [x + w // 2, y + h // 2]
        height, width = img.shape[:2]
        X = x + w // 2 - width / 2
        Y = y + h // 2 - height / 2
        # delta = (facePosition(1)-width, facePosition(2)-height)
        cv2.putText(img, str("dx={}, dy={}".format(X, Y)), (x, int(y + (1.1 * h))), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                    (0, 255, 0), 1)
        #print("x=", X, " y=", (y + h // 2 - height / 2))

    #cv2.imshow("Result", img)
    cv2.waitKey(1)
def cropFace(img, faces):
    for (x, y, w, h) in faces:
        img_crop=img[y:y+h, x:x+w]
        img_crop=scale_pic(img_crop,100*(img_crop.shape[1]/img.shape[1]))
        cv2.imshow("cropped image", img_crop)
        cv2.waitKey(1)


faceCascade = cv2.CascadeClassifier("Resources/haarcascades/haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
texts = ("right eye", "left eye", "null", "nothing", "null", "null", "null", "null", "null", "null",)

while True:

    ret, img = cap.read()
    img = scale_pic(img, 100)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    findFace(img, faces)
    cropFace(img, faces)