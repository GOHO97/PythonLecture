# -*- coding:utf-8 -*-
from time import sleep
from pymongo.mongo_client import MongoClient
from pymongo import ASCENDING

f, con = None, None
try:
    con = MongoClient("192.168.0.158")
    db = con.metaverseForKakao
    f = open("D:/csvdict/metaversData/kakaoBlog.txt", "a", encoding="utf-8") 
    
    blogData = db.blogData.find().sort([("date", ASCENDING), ("blogname", ASCENDING)])
    b = None
    for b in blogData:
        f.write("%d\t%d\t%d\t%s\t%s\t%s\t%s\n" % (
            b['date'].month,
            b['date'].day,
            b['date'].hour,
            b['blogname'],
            b['url'],
            b['_id'],
            b['contents'],
            ))
    print("성공")    
except Exception as e:
    print(e)
    sleep(10)

f.close()
con.close()
