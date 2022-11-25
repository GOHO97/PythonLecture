# -*- coding:utf-8 -*-
import pandas as pd
from http.client import HTTPConnection
from json import loads

#http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/json/IndividualServiceChargeService/1/1000/
huc, f = None, None
i, rb, data = None, None, None
try:
    huc = HTTPConnection("openapi.seoul.go.kr:8088")
    f = open("D:/csvdict/individualService/data.csv", "a", encoding="utf-8")
    
    for i in range(1, 7001, 1000):
        huc.request("GET", "/575a4655496b636839386f58586542/json/IndividualServiceChargeService/%d/%d/" % (i, i + 999))
        rb = huc.getresponse().read()
        data = loads(rb)["IndividualServiceChargeService"]["row"]
        
        # 업종, 주소, 품목, 가격
        for d in data:
            f.write("%s,%s,%s,%d\n" % (
                d["INDUTY_DESC"].replace(",", "."),
                d["ADRES_CN2"].replace(",", "."),
                d["PRDLST_DESC"].replace(",", "."),
                d["PC"]
                ))
            
        print(i)
    print("완료")
except Exception as e:
    print(e)

f.close()
huc.close()