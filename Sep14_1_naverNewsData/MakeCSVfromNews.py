# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient
from time import sleep
from pymongo import ASCENDING

con, f = None, None
try:
    con = MongoClient("192.168.0.158")
    db = con.naverNews
    news = db.news.find().sort([("nN_title", ASCENDING)])
    
    f = open("D:/csvdict/politicsNews/news.txt", "a", encoding="utf-8")
    
    n = None
    for n in news:
        f.write("%s\t%s\n" % (n["nN_title"], n["nN_text"]))
        
except Exception as e:
    print(e)
    sleep(10)
    
f.close()
con.close()
