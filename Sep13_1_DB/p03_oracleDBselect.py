# -*- coding:utf-8 -*-
from cx_Oracle import connect

con = connect("sleep/1@sdgn-djvemfu.tplinkdns.com:19195/xe")

sql="select * from HO_SIMPLETABLE where st_price = (select min(st_price) from HO_SIMPLETABLE)"

cur = con.cursor()

cur.execute(sql)

for name, price in cur:
    print(name, price)

cur.close()
con.close()
