import cv2 as cv
import numpy as np

__author__ = "jjnanthakumar477@gmail.com"


class Detections:
    ''' Image must be a matrix with pixels and it should not be empty'''

    def __init__(self, img, xmlpath=r'C:\Users\Nanthakumar J J\Desktop\projects\Tkinter GUI\FaceDetect\haarcascades\cascade_fontfaces_trained.xml', minneighbours=4):
        self.img = img
        self.grey = cv.cvtColor(code=cv.COLOR_BGR2GRAY, src=img)
        self.neigh = minneighbours
        self.xml = xmlpath

    def drawRectFace(self, scale=1.1):
        '''We have given some trianed faces xml file and if u need your own then train it using opencv and override this method'''
        face_cascade = cv.CascadeClassifier(self.xml)
        faces = face_cascade.detectMultiScale(self.grey, scaleFactor=scale, minNeighbors=self.neigh)
        for x, y, w, h in faces:
            cv.rectangle(self.img, (x, y), (x + w, y + h), (0, 0, 255), 4)
        return self.img

    def drawCircleeyes(self, color=(0, 0, 255), scale=1.2):
        '''We have given some trianed eyes xml file and if u need your own then train it using opencv and override this method'''

        face_cascade = cv.CascadeClassifier(self.xml)
        faces = face_cascade.detectMultiScale(self.grey, scaleFactor=scale, minNeighbors=self.neigh)
        eye_cascade = cv.CascadeClassifier(r'C:\Users\Nanthakumar J J\Desktop\projects\Tkinter GUI\FaceDetect\haarcascades\haarcascade_eye_tree_eyeglasses.xml')
        for x, y, w, h in faces:
            roi_gray = self.grey[y:y + h, x:x + w]
            roi_color = self.img[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=scale)
            for ex, ey, ew, eh in eyes:
                cv.circle(roi_color, (ex + ew // 2, ey + eh // 2), 20, color, 4)
        return self.img

    def showImage(self):
        cv.imshow('Detected', self.img)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def showVideoFrame(self, cap):
        '''For Video Frame capture argument is must'''
        cv.imshow('Detected', self.img)
        k = cv.waitKey(100)
        if cv.getWindowProperty('Detected', cv.WND_PROP_VISIBLE) < 1:
            cv.destroyAllWindows()
            cap.release()
        if k == 27:
            cv.destroyAllWindows()
            cap.release()
    def print(self):
        print(self.xml)
        print(self.img)

# sample workings
# img = cv.imread('../../FaceDetection/samples/group_faces.jpg')
# f = Detections(img, minneighbours=5)
# cap = cv.VideoCapture(0)
# while cap.isOpened():
#     _, frame = cap.read()
#     f = Detections(frame)
#     f.drawRectFace()
#     f.drawCircleeyes(scale=1.2, color=(0, 255, 0))
#     f.showVideoFrame(cap)
# f.drawRectFace(scale=1.1)
# f.drawCircleeyes(scale=1.4, color=(0, 255, 0))  # u can modify scale factors and neghbours also
# f.showImage()
# print("Created by " + __author__)
# print(cv.__file__)
# C:\Users\Nanthakumar J J\Desktop\projects\Tkinter GUI\venv\lib\site-packages\cv2\cv2.cp38-win_amd64.pyd