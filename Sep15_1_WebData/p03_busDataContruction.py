# -*- coding:utf-8 -*-
#http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/json/CardBusStatisticsServiceNew/1/1000/20150101/
from http.client import HTTPConnection
from json import loads
from time import sleep

f, huc = None, None
frontC, month, day, bd = None, None, None, None
try:
    huc = HTTPConnection("openapi.seoul.go.kr:8088")
    year = 2016;
    f = open(("D:/csvdict/busData/busCSV%d.txt" % year), "a", encoding="utf-8")
    for month in range(1,13):
        for day in range(1,32):
            for frontC in range(1,40001,1000):
                try:
                    huc.request("GET", "/575a4655496b636839386f58586542/json/CardBusStatisticsServiceNew/%d/%d/%d%02d%02d/" % (frontC, frontC+999, year, month, day))
                    resbody = huc.getresponse().read()
                    busData = loads(resbody)["CardBusStatisticsServiceNew"]["row"]
                    #년,월,일,정류장이름,노선,승차,하차
                    for bd in busData:
                        f.write("%d,%02d,%02d,%s,%s,%.0f,%.0f\n" % (
                            year,month,day,
                            bd["BUS_ROUTE_NM"].replace(",", " "),
                            bd["BUS_STA_NM"].replace(",", " "),
                            bd["RIDE_PASGR_NUM"],
                            bd["ALIGHT_PASGR_NUM"]
                            ))
                except KeyError:
                    continue
            print(day,"성공")
                    
except Exception as e:
    print(e)
    sleep(10)
    
f.close()
huc.close()