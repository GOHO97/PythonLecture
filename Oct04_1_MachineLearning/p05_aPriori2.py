# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient
from sys import maxunicode
from unicodedata import category
from konlpy.tag._okt import Okt
from hanspell.spell_checker import check
from apyori import apriori
from nltk.corpus.reader.ieer import titles

o = Okt()
con = MongoClient("192.168.0.158")
db = con.naverMovie

trainData = []
titles = []
for rd in db.reviewData.find():
    try:
        review = o.normalize(rd["review"])
        review = check(review).checked
        d = [rd["title"]]
        titles.append(rd["title"])
        for w, _ in o.pos(review, stem=True):
            d.append(w)
            
        trainData.append(d)
    except:
        pass
con.close()

titles = list(set(titles))
print(titles)

result = apriori(trainData, min_support=0.05, min_confidence=0.05)
for r in list(result):
    for r2 in r.ordered_statistics:
        l = list(r2.items_base)
        if len(l) == 1 and l[0] in titles:
            print(r2.items_base)
            print(r2.items_add)
            print(r2.confidence)
            print("-------")
