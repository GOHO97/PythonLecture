# -*- coding:utf-8 -*-
import pandas as pd
from http.client import HTTPConnection
from json import loads

huc = HTTPConnection("openapi.seoul.go.kr:8088")
huc.request("GET", "/575a4655496b636839386f58586542/json/RealtimeCityAir/1/25")
rb = huc.getresponse().read()
dustData = loads(rb)["RealtimeCityAir"]["row"]
df = pd.DataFrame(dustData)
huc.close()

df = df[["MSRRGN_NM", 'MSRSTE_NM', "PM10", "PM25", "IDEX_NM"]]
df["PM_SUM"] = df["PM10"] + df["PM25"]

df = df.set_index(df["MSRSTE_NM"])
df = df.sort_values(by="PM_SUM", ascending=False)
#print(df)

df["MSRSTE_NM"] = df["MSRSTE_NM"].replace("강남구", "학원")
#print(df)

df["PM_SUM"] = df["PM_SUM"].astype(str).replace("0.0", "없음")
print(df)
