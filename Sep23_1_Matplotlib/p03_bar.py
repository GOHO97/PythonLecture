# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from cx_Oracle import Connection

fontFile = "C:/Windows/Fonts/malgun.ttf"
# 설치된 폰트파일 경로
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
# 폰트명
plt.rc("font", family=fontName)

yData = np.array([10, 30, 44, 2, 45])
yData2 = np.array([5, 11, 40, 23, 10])
xLabel = ["일", "이", "삼", "사", "오"] # xData 쪽에 나오게 하고 싶은 데이터
xData = np.arange(len(xLabel)) # 위 처럼 해놓고 그냥 arange로 때워버림


#plt.bar(xData, yData, color='red', width=0.3, edgecolor="blue", linewidth=3)
#colors = ["#FBE9E7", "#FFCCBC", "#FFAB91", "#FF8A65", "#FF7043"]
#plt.bar(xData, yData, width=0.3, align="edge") # 첫 데이터가 0, 10인 상황
#plt.bar(xData-0.3, yData2, width=0.3, align="edge", color="blue")# 첫데이터 -0.7, 5
# x의 값을 일부러 빼줘서 기존 바 보다 앞에 가서 그릴 수 있게 해줌으로 겹쳐지지 않게 함.

plt.bar(xData, yData, color="orange")
plt.bar(xData, yData2, color="pink", bottom=yData)

plt.show()



