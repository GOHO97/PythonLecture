# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from json import loads
from cx_Oracle import connect

huc, con = None, None
try:
    con = connect("sleep/1@sdgn-djvemfu.tplinkdns.com:19195/xe")
    cur = con.cursor()
    
    huc = HTTPSConnection("api.openweathermap.org")
    huc.request("GET", "/data/2.5/weather?q=seoul&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr")
    resbody = huc.getresponse().read()
    weatherData = loads(resbody)
    
    sql = "insert into ho_openWeatherData values('%s', %.2f, %d, sysdate)" % (
        weatherData["weather"][0]["description"],
        weatherData["main"]["temp"],
        weatherData["main"]["humidity"]) 
    
    cur.execute(sql)
    if cur.rowcount == 1:
        print("성공")
        con.commit()
    
except Exception as e:
    print(e)

huc.close()
cur.close()
con.close()
    