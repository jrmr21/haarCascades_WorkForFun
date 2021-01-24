#!/usr/bin/env python3

path = '/home/jrmr/Bureau/pyMachinLearning/haarCascades_WorkForFun/'


import numpy as np
import cv2
from matplotlib import pyplot as plt


penguin_cascade = cv2.CascadeClassifier(path+'cascade_test/cascade.xml')

img = cv2.imread(path+'cascade_test/img5.jpg')
img = cv2.resize(img, (640, 420), 0)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#penguin = penguin_cascade.detectMultiScale(gray, 1.26, 9) #4.15
penguin = penguin_cascade.detectMultiScale(gray, 4.15, 45, minSize =(75,75))

for (x,y,w,h) in penguin:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    print(len(penguin))

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()