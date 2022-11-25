# -*- coding:utf-8 -*-
import pandas as pd
from sklearn.cluster._kmeans import KMeans
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fontFile = "C:/Windows/Fonts/malgun.ttf"
# 설치된 폰트파일 경로
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
# 폰트명
plt.rc("font", family=fontName)
#지하철 csv 역별로 탄 사람 평균, 내린 사람 평균
#10그룹으로 나눠서
df = pd.read_csv("D:/csvdict/subwayData/seoulSubway.txt", names=["년", '월', '일', '호선', '역', '승차자', '하차자'])
df2 = pd.DataFrame()
df = df.groupby("역")[["승차자", '하차자']].mean()

trainData = df[["승차자", "하차자"]].to_numpy()
km = KMeans(10)
df["그룹"] = km.fit_predict(trainData)
#print(df)
#sns.scatterplot(data=df, x='승차자', y="하차자", hue="그룹", palette='coolwarm')
#plt.show()

what = input("역명 : ")
print(df[df['그룹'] == df.loc[what]["그룹"]])
# 입력 받고 그거랑 같은 그룹에 속한 역들