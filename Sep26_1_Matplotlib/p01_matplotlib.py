# -*- coding:utf-8 -*-
# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/json/CardSubwayPayFree/1/1000/201501
from http.client import HTTPConnection
from json import loads

huc = HTTPConnection("openapi.seoul.go.kr:8088")
f = open("D:/csvdict/subwayData/freeRide.csv", "a", encoding="utf-8")
rb, data = None, None
year, month, d = None, None, None
for year in range(2015, 2022, 1): 
    for month in range(1, 13, 1):
        huc.request("GET", "/575a4655496b636839386f58586542/json/CardSubwayPayFree/1/1000/%d%02d" % (year, month))
        rb = huc.getresponse().read()
        data = loads(rb)["CardSubwayPayFree"]["row"]
        # 년월,호선,역명,유임승차,무임승차,유임하차,무임하차
        for d in data :
            f.write("%d%02d,%s,%s,%d,%d,%d,%d\n" % (
                year, month,
                d["LINE_NUM"],
                d["SUB_STA_NM"],
                d["PAY_RIDE_NUM"],
                d["FREE_RIDE_NUM"],
                d["PAY_ALIGHT_NUM"],
                d["FREE_ALIGHT_NUM"]
                ))
huc.close()
f.close()