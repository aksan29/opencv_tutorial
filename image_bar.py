import pyzbar.pyzbar as pyzbar
import matplotlib.pyplot as plt
import numpy as np
import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input',type=str)
args = parser.parse_args()

img = cv2.imread(args.input)
objectDecoded = pyzbar.decode(img)
for obj in objectDecoded:
    print(obj.data)
