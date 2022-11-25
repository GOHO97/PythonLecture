# -*- coding:utf-8 -*-
import pandas as pd
from http.client import HTTPConnection
from json import loads

huc = HTTPConnection("openapi.seoul.go.kr:8088")
huc.request("GET", "/575a4655496b636839386f58586542/json/RealtimeCityAir/1/25")
rb = huc.getresponse().read()
dustData = loads(rb)["RealtimeCityAir"]["row"]

df = pd.DataFrame(dustData)
print(df)

huc.close()