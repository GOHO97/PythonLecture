# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/xml/MosquitoStatus/1/5/2016-06-28
year, month, day = None, None, None
f = open("D:/csvdict/mosquitoData/mosquito.csv", "a", encoding="utf-8")
huc = HTTPConnection("openapi.seoul.go.kr:8088")
for year in range(2016, 2023):
    for month in range(5, 11):
        for day in range(1, 32):
            huc.request("GET", "/575a4655496b636839386f58586542/xml/MosquitoStatus/1/1/%d-%02d-%02d" % (year, month, day))
            rb = huc.getresponse().read()
            mosquito = fromstring(rb).find("row")
            # 년, 월, 일, 수변부, 주거지, 공원
            if mosquito != None:
                f.write("%d-%02d-%02d,%s,%s,%s\n" %
                        (year, month, day,
                         mosquito.find("MOSQUITO_VALUE_WATER").text,
                         mosquito.find("MOSQUITO_VALUE_HOUSE").text,
                         mosquito.find("MOSQUITO_VALUE_PARK").text
                         ))
    print(year)
f.close()
huc.close()