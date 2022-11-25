# -*- coding:utf-8 -*-
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from http.client import HTTPConnection
from json import loads

fontFile = "C:/Windows/Fonts/malgun.ttf"
# 설치된 폰트파일 경로
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
# 폰트명
plt.rc("font", family=fontName)

huc = HTTPConnection("openapi.seoul.go.kr:8088")
huc.request("GET", "/575a4655496b636839386f58586542/json/RealtimeCityAir/1/25")
rb = huc.getresponse().read()
dustData = loads(rb)["RealtimeCityAir"]["row"]
huc.close()
df = pd.DataFrame(dustData)
#sns.barplot(x="MSRRGN_NM", y="PM10", data=df, palette="Accent")
# 통계가 필요하다 싶으면 알아서 통계 내줌, 권역별 PM10의 평균
# 검은막대는 신뢰구간 95%

sns.countplot(x="MSRRGN_NM", hue="IDEX_NM", data=df, palette="autumn")
# 권역별 몇 개 dlswl, 상태별로 나눠서 다른색으로 표시
plt.xticks(rotation=45)
plt.show()