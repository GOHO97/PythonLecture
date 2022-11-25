# -*- coding:utf-8 -*-
from _datetime import datetime
from http.client import HTTPConnection
from time import sleep
from xml.etree.ElementTree import fromstring


hc, f, y, m, d = None, None, None, None, None
try:
    f = open("D:/csvdict/subwayData/seoulSubway.txt", "a", encoding="utf-8")
    hc = HTTPConnection("openapi.seoul.go.kr:8088")
    
    for y in range(2015, 2022):
        for m in range(1, 13):
            for d in range(1, 32):
                when = "%d%02d%02d" % (y, m, d)
                hc.request("GET", "/575a4655496b636839386f58586542/xml/CardSubwayStatsNew/1/602/" + when)
                resBody = hc.getresponse().read()
                subwayData = fromstring(resBody).getiterator("row")
                    
                sd, text, date = None, None, None
                for sd in subwayData:
                    date = sd.find("USE_DT").text
                    f.write("%s,%s,%s,%s,%s,%s,%s\n" % (
                        date[0:4],
                        date[4:6],
                        date[6:8],
                        sd.find("LINE_NUM").text.replace(",", " "),
                        sd.find("SUB_STA_NM").text.replace(",", " "),
                        sd.find("RIDE_PASGR_NUM").text,
                        sd.find("ALIGHT_PASGR_NUM").text
                        ))
                print(when)
    
    print("성공")
except Exception as e:
    print(e)
    sleep(10)

f.close()    
hc.close()