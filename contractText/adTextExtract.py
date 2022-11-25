# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import ssl

header = {"User-agent": "Mozilla/5.0"} 
ssl.match_hostname = lambda cert, hostname: True
ssl._create_default_https_context = ssl._create_unverified_context

urlTxt = open("D:/haheehoData/urlList.txt", "r", encoding="utf-8") 
pKeywordTxt = open("D:/haheehoData/pKeyword.txt", "a", encoding="utf-8")

def getMainFrameSrc(url):
    global header
    req = requests.get(url, headers=header)
    bs = BeautifulSoup(req.text, "html.parser")
    realAddr = bs.select('#mainFrame')[0]["src"]
    
    return realAddr


def getMainContainer(realAddr):
    global header
    
    req = requests.get("https://blog.naver.com%s" % realAddr, headers=header)
    bs = BeautifulSoup(req.text, "html.parser")
    pList = None
    try:
        pList = bs.select(".se-text-paragraph")
    except:
        pass
    return pList


urlT = urlTxt.readlines()
no, url, pList, n, p, text = None, None, None, None, None, None

for no, url in enumerate(urlT):
    url = url.replace("\n", "")
    pList = getMainContainer(getMainFrameSrc(url))
    
    for n, p in enumerate(reversed(pList)):
        if n == 3:
            break
        text = p.text
        if not text.__contains__("@") and not text.__contains__("#"):
            pKeywordTxt.write("%s\n" % text.replace("\n", ""))
        
    print(no)
            
pKeywordTxt.close()
urlTxt.close()
