# -*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

fontFile = "C:/Windows/Fonts/malgun.ttf"
# 설치된 폰트파일 경로
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
# 폰트명
plt.rc("font", family=fontName)

df = pd.read_csv("D:/csvdict/subwayData/freeRide.csv", names=["DATE", "LINE", "STATION", "PRN", "FRN", "PAN", "FAN"])
df = df.set_index("LINE")
df = df.groupby("LINE")[["PRN", "FRN", "PAN", "FAN"]].mean()

lineLabel = df.index
lineData = np.arange(len(lineLabel))
#x축에 넣기 위한 것 arrange에는 숫자가 들어가야 되고 호선으로 x축을 쓰겠다는 말
# 위 2가지를 xticks으로 넣어 줌으로써 x축으로 쓸 수 있게 됨.
prn = np.array(df["PRN"])
frn = np.array(df["FRN"])
pan = np.array(df["PAN"])
fan = np.array(df["FAN"])

f = frn + fan
f = (f/f.max()) * 500


plt.scatter(prn, pan, s=f, color="green", alpha=0.3)
# 많이 내고 타면, 많이 내고 내리는데, 그냥 시리즈랑은 무관함
plt.title("지하철")
plt.show()