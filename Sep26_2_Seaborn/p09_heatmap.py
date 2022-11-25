 # -*- coding:utf-8 -*-
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fontFile = "C:/Windows/Fonts/malgun.ttf"
# 설치된 폰트파일 경로
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
# 폰트명
plt.rc("font", family=fontName)

df = pd.read_csv("D:/csvdict/subwayData/seoulSubway.txt", names=['년','월','일','노선','역명','승차자','하차자'])
df['이용객수']= df['승차자'] + df['하차자']
pt = df.pivot_table(index='노선', columns='월', values='이용객수')

sns.heatmap(pt, cmap='summer')
plt.show()