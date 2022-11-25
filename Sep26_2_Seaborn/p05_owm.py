# -*- coding:utf-8 -*-
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from cx_Oracle import connect

fontFile = "C:/Windows/Fonts/malgun.ttf"
# 설치된 폰트파일 경로
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
# 폰트명
plt.rc("font", family=fontName)

db = None
try :
    db = connect("sleep/1@sdgn-djvemfu.tplinkdns.com:19195/xe")
    sql = "select * from owm_weather_kwon order by OWM_DATE"
    df = pd.read_sql(sql, db)
    print(df)
    #df = df.sort_values(by="OWM_DATE")
    
except Exception as e:
    print(e)

db.close()

sns.scatterplot(data=df, x='OWM_TEMP', y='OWM_HUMI', hue="OWM_DESC", size="OWM_HUMI", palette='magma')
plt.show()