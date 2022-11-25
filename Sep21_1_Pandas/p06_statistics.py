# -*- coding:utf-8 -*-
import pandas as pd
from cx_Oracle import Connection

con = None
try :
    con = Connection("sleep/1@sdgn-djvemfu.tplinkdns.com:19195/xe")
    sql = "select * from kma_weather_kwon"
    df = pd.read_sql(sql, con)
    print(df.groupby("KW_WFKOR")['KW_TEMP'].mean())
except Exception as e:
    print(e)
    
con.close()