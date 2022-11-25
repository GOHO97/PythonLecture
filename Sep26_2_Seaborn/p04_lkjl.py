# -*- coding:utf-8 -*-
import seaborn as sns
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
df["P"] = df["PRN"] + df["PAN"]
sns.scatterplot(data = df, x='PRN', y='PAN', size='P', hue='LINE', palette='coolwarm')
plt.show()