# -*- coding:utf-8 -*-
import pandas as pd
from sklearn.cluster._kmeans import KMeans
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from sklearn.neighbors._classification import KNeighborsClassifier

fontFile = "C:/Windows/Fonts/malgun.ttf"
# 설치된 폰트파일 경로
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
# 폰트명
plt.rc("font", family=fontName)

# kMeans: k개의 평균

df = pd.DataFrame()
df['싸움'] = [80, 95, 10, 90, 5]
df['욕'] = [20, 5, 90, 10, 95]

trainData = df[['싸움', '욕']].to_numpy()
print(trainData)

km = KMeans(2) # 몇 그룹으로 나눌건가
print(km.fit_predict(trainData))

df['그룹'] = km.fit_predict(trainData)
print(df)

#sns.scatterplot(x='싸움', y='욕', hue='그룹', data=df, palette='autumn')
#plt.show()

a = float(input("싸움 : "))
b = float(input("욕 : "))
label = df['그룹'].to_numpy()

knc = KNeighborsClassifier(3)
knc.fit(trainData, label)

newdata = np.array([[a, b]])
print(knc.predict(newdata)[0])


