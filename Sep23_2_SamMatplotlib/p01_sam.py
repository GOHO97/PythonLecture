# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fontFile = "C:/Windows/Fonts/malgun.ttf"
# 설치된 폰트파일 경로
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
# 폰트명
plt.rc("font", family=fontName)

df = pd.read_csv("D:/csvdict/samResult.txt", sep="\t", names=["누구", "몇번"])
df = df.sort_values(by='몇번', ascending=False)

name = df['누구']
count = df['몇번']
colors2 = ['#3949AB', '#43A047', '#E53935']
e = [0, 0.1, 0]
d = {"width":0.7, "edgecolor":"black", "linewidth":3}

plt.pie(count, labels=name, autopct="%.1f%%", colors=colors2, explode=e, startangle=180, wedgeprops=d)
plt.title("삼국지")
plt.show()


