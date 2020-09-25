# -*- coding: utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt

img_size =28

img = cv2.imread('35.png')

edges = cv2.Canny(img,100,200)
blur = cv2.blur(edges,(5,5))

#mask_eroded = cv2.erode(blur, None, iterations=10)
mask_eroded_dilated = cv2.dilate(blur, None, iterations=4)

cnts, hiers = cv2.findContours(mask_eroded_dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]

cnts = [x for x in cnts if len(x)>30]

detection = np.copy(mask_eroded_dilated)

for cnt in cnts:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(detection, (x, y), (x + w, y + h), (255, 0, 0), 5)  # blue
    crop_img = detection[y:y + h, x:x + w]
    resizedImg = cv2.resize(crop_img, (img_size, img_size))
    cv2.imshow("crop resizedImg", resizedImg)
    cv2.waitKey(20)



plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(detection,cmap = 'gray')
plt.title('Detection Image'), plt.xticks([]), plt.yticks([])
plt.show()







