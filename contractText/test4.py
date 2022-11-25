# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import ssl
from konlpy.tag._okt import Okt 
import time
from pymongo.mongo_client import MongoClient
from _io import StringIO

start = time.time()

header = {"User-agent": "Mozilla/5.0"} 
ssl.match_hostname = lambda cert, hostname: True

urlTxt = open("D:/haheehoData/urlList.txt", "r", encoding="utf-8") 

def getMainFrameSrc(url):
    global header
    req = requests.get(url, headers=header)
    bs = BeautifulSoup(req.text, "html.parser")
    realAddr = bs.select('#mainFrame')[0]["src"]
    
    return realAddr


def getMainContainer(realAddr):
    global header
    mainContainer = None
    req = requests.get("https://blog.naver.com" + realAddr, headers=header)
    bs = BeautifulSoup(req.text, "html.parser")
    try:
        mainContainer = bs.select(".se-main-container")[0]
    except:
        mainContainer = bs.select("#postViewArea")[0]
    
    return mainContainer.text.replace("\n", " ").replace("\u200b", "")
  
urlT = urlTxt.readlines()
o = Okt()

testText = "하희호에 오신것을 환영합니다."
testText = o.normalize(testText)
print(time.time() - start)
testText = o.pos(testText, stem=True)
print(time.time() - start)

con = MongoClient("192.168.0.141")
db = con.xe

no, u, totalText, word, pos,  = None, None, None, None, None
cleanText = []
for no, u in enumerate(urlT):
    
    if no == 3:
        break
    cleanText = []
    
    totalText = getMainContainer(getMainFrameSrc(u))
    print(time.time() - start)
    totalText = o.normalize(totalText)
    print(time.time() - start)
    totalText = o.pos(totalText, stem=True)
    print(time.time() - start)
    
    for word, pos in totalText:
        cleanText.append("%s " % word)
        
    d = {"cd_content" : "".join(cleanText), "cd_label": "광고", "cd_like_count" : 0}
    db.haheeho.insert_one(d)
    print(time.time() - start)

urlTxt.close()
con.close()