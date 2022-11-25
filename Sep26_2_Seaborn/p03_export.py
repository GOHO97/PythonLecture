 # -*- coding:utf-8 -*-
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from cx_Oracle import connect
from _datetime import datetime

fontFile = "C:/Windows/Fonts/malgun.ttf"
# 설치된 폰트파일 경로
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
# 폰트명
plt.rc("font", family=fontName)

df = pd.read_csv("D:/csvdict/subwayData/seoulSubway.txt", names=['년','월','일','노선','역명','승차자','하차자'])

def getYoil(d):
    d = "%04d%02d%02d" % (d["년"],d["월"],d["일"])
    d = datetime.strptime(d, "%Y%m%d")
    return datetime.strftime(d, '%a')

df["이용객수"] = df["승차자"] + df["하차자"] 
df["요일"] = df.apply(getYoil, axis=1)

sns.violinplot(data= df, x='요일', y='이용객수')
plt.show()