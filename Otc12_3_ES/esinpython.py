# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from json import dumps

hc = HTTPConnection("192.168.0.125:9200")

h = {"Content-Type":"application/json; charset=utf-8"}
reqBody ={
  "query":{
    "match_all": {}
  }
}
# loads는 json을 python collection으로 만들어줬었고
# dumps는 python collection을 json으로 만들어준다.
reqBody = dumps(reqBody)

hc.request("POST", "/oct12_menu/_search", reqBody, h)
resBody = hc.getresponse().read()
print(resBody.decode())

hc.close()