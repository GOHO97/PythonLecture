# -*- coding:utf-8 -*-
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
df = pd.DataFrame(dustData)
huc.close()

loc = df["MSRSTE_NM"].to_numpy()
pm10 = df["PM10"].to_numpy()
pm25 = df["PM25"].to_numpy()

xData = np.arange(len(loc))

plt.bar(xData, pm10, color="#7E57C2")
plt.bar(xData, pm25, color="#26A69A", bottom=pm10)
plt.xticks(xData, loc)
plt.title("실시간 미세먼지")
plt.show()