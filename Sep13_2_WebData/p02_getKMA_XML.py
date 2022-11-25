# -*- coding:utf-8 -*-
from cx_Oracle import connect
from http.client import HTTPSConnection
from xml.etree.ElementTree import fromstring

huc = None
con = None
cur = None
try:
    huc = HTTPSConnection("www.kma.go.kr")
    huc.request("GET", "/wid/queryDFS.jsp?x=49&y=37")
    res = huc.getresponse()
    resBody = res.read()
    
    
    weatherXML = fromstring(resBody)
    weathers = weatherXML.getiterator("data")

    con = connect("sleep/1@sdgn-djvemfu.tplinkdns.com:19195/xe")
    cur = con.cursor()
    
    time = None
    temp = None
    weather = None
    sql = None
    
    for w in weathers:
        if w.find("day").text == "1":
            break
        time = w.find("hour").text
        temp = w.find("temp").text
        weather = w.find("wfKor").text
        sql ="insert into ho_kmaData values(%s, %s, '%s', sysdate)" % (time, temp, weather)
        cur.execute(sql)
    
    con.commit()
    print("끝")
    
except Exception as e:
    print(e)        

huc.close() 
cur.close()
con.close()


# DB연결