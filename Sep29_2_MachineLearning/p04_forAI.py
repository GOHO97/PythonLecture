# -*- coding:utf-8 -*-
import cv2
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

data = cv2.imread("D:/a4.jpg", cv2.IMREAD_COLOR)
avgColor = cv2.mean(data)

r = "%02X" % int(avgColor[2])
g = "%02X" % int(avgColor[1])
b = "%02X" % int(avgColor[0])
# 16진수로 뽑아줌.
c = "#"+ r + g + b
print(avgColor)
print(r,g,b)
plt.bar(10, 10, color=c)
plt.show()