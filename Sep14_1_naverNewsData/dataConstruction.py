# -*- coding:utf-8 -*-

from http.client import HTTPSConnection
from time import sleep
from urllib.parse import quote
from xml.etree.ElementTree import fromstring
from stringCleaner import StringCleaner
from pymongo.mongo_client import MongoClient

hc, con = None, None
try:
    con = MongoClient("192.168.0.158")
    db = con.naverNews
    
    
    q = quote("김건희")
    h = {"X-Naver-Client-Id": "hDC5lYO9N9IbJg63cS_u",
         "X-Naver-Client-Secret": "dksK6IXgpK"}
    
    hc = HTTPSConnection("openapi.naver.com")
    hc.request("GET", "/v1/search/news.xml?query=" + q, headers=h)
    resBody = hc.getresponse().read()
    
    
    r = None
    for n in fromstring(resBody).getiterator("item"):
        r = db.news.insert_one({
            "nN_title": StringCleaner.clean(n.find("title").text),
            "nN_text": StringCleaner.clean(n.find("description").text)
            })
        if r.acknowledged:
            print("성공")
        
except Exception as e:
    print(e)
    sleep(10)
    
hc.close()
con.close()

