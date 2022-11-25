# -*- coding:utf-8 -*-
import os
import cv2

def getImg(folder, w, h):
    datas = []
    for f in os.listdir(folder):
        data = cv2.imread(folder + "/" + f, cv2.IMREAD_GRAYSCALE)
        data = cv2.resize(data, (w, h))
        data = data.flatten()
        datas.append(data)
    return datas

