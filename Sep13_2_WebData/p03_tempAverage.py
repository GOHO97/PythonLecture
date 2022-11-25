# -*- coding:utf-8 -*-
from cx_Oracle import connect

con = connect("sleep/1@sdgn-djvemfu.tplinkdns.com:19195/xe")

sql = "select hk_time, avg(hk_temp) from ho_kmaData group by hk_time order by hk_time"
cur = con.cursor()
cur.execute(sql)

for h, t in cur:
    print(h, t)
    
cur.close()
con.close()

