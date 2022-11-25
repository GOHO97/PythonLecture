# -*- coding:utf-8 -*-
#http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/json/ListNecessariesPricesService/1/1000/
from http.client import HTTPConnection
from json import loads

huc, f, i, d = None, None, None, None
try:
    huc = HTTPConnection("openapi.seoul.go.kr:8088")
    f = open("D:/csvdict/marketData/market.csv", "a", encoding="utf-8")
    for i in range(1, 403001, 1000):
        huc.request("GET", '/575a4655496b636839386f58586542/json/ListNecessariesPricesService/%d/%d/' % (i, i + 999))
        rb = huc.getresponse().read()
        try:
            data = loads(rb)["ListNecessariesPricesService"]["row"]
            for d in data:
                f.write("%s,%s,%s,%s,%s" % (d["M_NAME"], d["A_NAME"].replace(",", ""), d["A_PRICE"], d["M_TYPE_NAME"], d["M_GU_NAME"]))
        except KeyError:
            continue
        print(i)
except Exception as e:
    print(e)
    
huc.close()
f.close()