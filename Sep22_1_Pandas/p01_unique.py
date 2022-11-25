# -*- coding:utf-8 -*-
import pandas as pd
from cx_Oracle import Connection

con = None
try :
    con = Connection("sleep/1@sdgn-djvemfu.tplinkdns.com:19195/xe")
    sql = "select * from kma_weather_kwon"
    df = pd.read_sql(sql, con)
    print(df["KW_WFKOR"].unique())
    print(df["KW_WFKOR"].value_counts())
except Exception as e:
    print(e)
    
con.close()