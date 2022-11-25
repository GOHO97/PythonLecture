# -*- coding:utf-8 -*-
import cv2
import matplotlib.pyplot as plt
import numpy as np

data = cv2.imread("D:/a4.jpg", cv2.IMREAD_GRAYSCALE)

_, data = cv2.threshold(data, 150, 255, cv2.THRESH_BINARY)

plt.imshow(data, cmap='gray')
plt.show()

