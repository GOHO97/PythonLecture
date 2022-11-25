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
yData = np.array(df["PRN"])
yData2 = np.array(df["FRN"])
yData3 = np.array(df["PAN"])
yData4 = np.array(df["FAN"])


plt.bar(lineData-0.3, yData2, width=0.3, align="edge", color="orange")
plt.bar(lineData-0.3, yData4, width=0.3, align="edge", color="pink", bottom=yData4)# 첫데이터 -0.7, 5
plt.bar(lineData, yData, width=0.3, align="edge", color="blue") # 첫 데이터가 0, 10인 상황
plt.bar(lineData, yData3, width=0.3, align="edge", color="skyblue", bottom=yData3)
# x의 값을 일부러 빼줘서 기존 바 보다 앞에 가서 그릴 수 있게 해줌으로 겹쳐지지 않게 함.
plt.xticks(lineData, lineLabel, rotation=45)
plt.legend(['그냥타', '그냥내려', '내고타', '내고내려'])
plt.show()