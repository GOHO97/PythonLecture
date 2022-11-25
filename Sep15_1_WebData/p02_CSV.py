# -*- coding:utf-8 -*-
from time import sleep
from cx_Oracle import connect

con = None
try:
    f = open("D:/csvdict/openweatherData/weather.txt", "a", encoding="utf-8")

    con = connect("sleep/1@sdgn-djvemfu.tplinkdns.com:19195/xe")
    cur = con.cursor()
    
    sql = "select * from ho_openWeatherData order by ho_date"
    cur.execute(sql)
    
    weather, temp, humidity, date = None, None, None, None
    for weather, temp, humidity, date in cur:
        f.write("%d,%d,%d,%d,%s,%.2f,%d\n" % (date.year, date.month, date.day, date.hour, weather, temp, humidity))

    print("성공")
except Exception as e:
    print(e)
    sleep(10)

cur.close()
con.close()
f.close