# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient

con = MongoClient("192.168.0.158")
db = con.xe

menus = db.snack2.find()

for m in menus:
    print(m)

con.close()

