import cv2
import matplotlib.pyplot as plt
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input',type=str)
args = parser.parse_args()

cascade_path = '/home/fajrin/CV/facedetection-master/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cascade_path)
img = cv2.imread(args.input)
def show_image(img):
    plt.figure(figsize=(15, 12))
    plt.imshow(cv2.cvtColor(img , cv2.COLOR_BGR2RGB))
    plt.show()

def face_detect(img) :
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray ,1.2,4)
    for x,y,h,w in faces :
        cv2.rectangle(img, (x,y) , (x+h ,y+w) , (255,0,0),2)
    show_image(img)

face_detect(img)
cv2.destroyAllWindows()