# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient

con = MongoClient("192.168.0.158")
db = con.xe

n = input("메뉴명 : ")
p = int(input("가격 : "))

r = db.snack2.insert_one({"m_name": n, "m_price": p})

if r.acknowledged:
    print("성공")


con.close()
