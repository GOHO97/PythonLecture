# -*- coding:utf-8 -*-
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fontFile = "C:/Windows/Fonts/malgun.ttf"
# 설치된 폰트파일 경로
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
# 폰트명
plt.rc("font", family=fontName)

df = pd.read_csv("D:/csvdict/busData/busYoilResult.csv", sep='\t', names=['뭐', '합계'])
print(df)
df2 = df[df['뭐'].str.endswith('수')]
df2['뭐'] = df2['뭐'].apply(lambda d:d.replace("_수", ""))
df2 = df2.set_index(df2['뭐'])
df3 = df[df['뭐'].str.endswith('합')]
df3['뭐'] = df3['뭐'].apply(lambda d:d.replace("_합", ""))
df3 = df3.set_index(df2['뭐'])
df4 = pd.DataFrame()
df4['뭐'] = df3['뭐']
df4['평균'] = df3['합계'] / df2['합계']
print(df4)

sns.barplot(data=df4, x='뭐', y='평균', palette='Accent')
plt.show()

