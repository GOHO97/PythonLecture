# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from urllib.parse import quote
from json import loads
from time import sleep
from pymongo.mongo_client import MongoClient
from _datetime import datetime
from stringCleaner import StringCleaner

#GET /v2/search/blog HTTP/1.1

huc, con = None, None
try:
    con = MongoClient("192.168.0.158")
    db = con.metaverseForKakao
    
    
    huc = HTTPSConnection("dapi.kakao.com")
    q = quote("메타버스")
    h = {"Authorization" : "KakaoAK f97c35a2dec2c919adebacba62e5bae2"}
    huc.request("GET", "/v2/search/blog?query=" + q + "&sort=recency", headers=h)
    resbody = huc.getresponse().read()
    blogs = loads(resbody)["documents"]
    
    now = datetime.today()
    blog = None
    for blog in blogs:
        db.blogData.insert_one({
            "blogname": StringCleaner.clean(blog["blogname"]),
            "url": StringCleaner.clean(blog["url"]),
            "_id": StringCleaner.clean(blog["title"]),
            "contents": StringCleaner.clean(blog["contents"]),
            "date" : now
            })

    print("성공")
except Exception as e:
    print(e)
    sleep(10)

con.close()
huc.close()