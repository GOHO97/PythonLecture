# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from http.client import HTTPSConnection, HTTPConnection

con = MongoClient("192.168.0.158")
db = con.metaverseForKakao

trainData = []
label = []
for mfk in db.blogData.find():
    trainData.append(mfk['blogname'] + ' ' + mfk['contents'])
    label.append(mfk['label'])
con.close()

cv = CountVectorizer()
cvResult = cv.fit_transform(trainData).toarray()
mnb = MultinomialNB().fit(cvResult, label)

#https://blog.naver.com/tkahr/222883643381
what = input("주소 : ")
what = what.split("/")
huc = None
if what[0] == "https:":
    huc = HTTPSConnection(what[2])
else:
    huc = HTTPConnection(what[2])

addr = "/"

for i in range(3, len(what)):
    addr += what[i] + "/"
    
huc.request("GET", addr)
rb = huc.getresponse().read()
huc.close()

whatResult = cv.transform([what]).toarray()
result = mnb.predict(whatResult)[0]
print(result)