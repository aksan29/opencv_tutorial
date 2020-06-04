import pandas as pd
import matplotlib.pyplot as plt
import cv2

path_image= '/home/fajrin/CV/bola.jpg'
img = cv2.imread(path_image)
def show_image(img):
    plt.figure(figsize=(15,12))
    plt.imshow(cv2.cvtColor(img , cv2.COLOR_BGR2RGB))
    plt.xticks([])
    plt.yticks([])
    plt.show()

show_image(img)