# -*- coding:utf-8 -*-
import pandas as pd
from cx_Oracle import connect
# 습도 필드 지우고
# 평균 기온 보다 높은 데이터 삭제

con = connect("sleep/1@sdgn-djvemfu.tplinkdns.com:19195/xe")
df = pd.read_sql("select * from owm_weather_kwon", con)

df = df[["OWM_DATE", "OWM_TEMP", "OWM_DESC"]]
df = df[df["OWM_TEMP"] <= df["OWM_TEMP"].mean()] 
print(df)

con.close()