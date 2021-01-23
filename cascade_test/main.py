

path = '/home/jrmr/Bureau/pyMachinLearning/haarCascades_WorkForFun/'


import numpy as np
import cv2
from matplotlib import pyplot as plt


penguin_cascade = cv2.CascadeClassifier(path+'cascade_test/penguin_cascade1.xml')

img = cv2.imread(path+'cascade_test/img5.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#penguin = penguin_cascade.detectMultiScale(gray, 1.26, 9)
penguin = penguin_cascade.detectMultiScale(gray, 5, 25)

for (x,y,w,h) in penguin:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()