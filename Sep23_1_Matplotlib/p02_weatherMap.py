# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from cx_Oracle import Connection

fontFile = "C:/Windows/Fonts/malgun.ttf"
# 설치된 폰트파일 경로
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
# 폰트명
plt.rc("font", family=fontName)

con = None
try :
    con = Connection("sleep/1@sdgn-djvemfu.tplinkdns.com:19195/xe")
    sql = "select * from owm_weather_kwon"
    df = pd.read_sql(sql, con)
    df = df.sort_values(by="OWM_DATE")
    
except Exception as e:
    print(e)
con.close()

def convertDate(d):
    return "%d일%d시" % (d.day, d.hour)

time = df["OWM_DATE"].apply(convertDate).to_numpy()
temp = df["OWM_TEMP"].to_numpy()
humi = df["OWM_HUMI"].to_numpy()

whole, sp1Conf = plt.subplots()
p1 = sp1Conf.plot(temp, "r-o")
sp1Conf.set_xlabel("언제")
sp1Conf.set_ylabel("기온")

sp2Conf = sp1Conf.twinx()
p2 = sp2Conf.plot(humi, "b-s")
sp2Conf.set_ylabel("습도")

plt.xticks(np.arange(len(time)), time)
plt.show()