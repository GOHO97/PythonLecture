# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient

con = MongoClient("192.168.0.158")
db = con.xe

p1 = int(input("얼마 이상 : "))
p2 = int(input("얼마 이하 : "))

w = {"$and" : [{"m_price":{"$gte":p1}, 'm_price':{"$lte" : p2}}]}

r = db.snack2.delete_many(w)
if r.deleted_count >= 1:
    print("성공")
    
con.close()
