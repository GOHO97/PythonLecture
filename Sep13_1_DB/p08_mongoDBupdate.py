# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient

con = MongoClient("192.168.0.158")
db = con.xe

n = input("메뉴명 : ")
p = int(input("가격 : "))

w = {"m_name": {"$regex": n}}
s = {"$set": {"m_price": p}}

r = db.snack2.update_many(w, s)
if r.modified_count >= 1:
    print("성공")

con.close()

