# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from xml.etree.ElementTree import fromstring


huc = HTTPSConnection("www.kma.go.kr")

huc.request("GET", "/wid/queryDFS.jsp?x=49&y=37")

res = huc.getresponse()
resBody = res.read()


huc.close()

weatherXML = fromstring(resBody)

weathers = weatherXML.getiterator("data") # <data></data>들

for w in weathers:
    print(w.find("hour").text)
    print(w.find("temp").text)
    print(w.find("wfKor").text)


    

    

