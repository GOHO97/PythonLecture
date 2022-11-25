# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
from PIL import Image
import urllib.request
from io import BytesIO
import pytesseract as pt
import time
import ssl

start = time.time()
header = {"User-agent": "Mozilla/5.0"} 
ssl.match_hostname = lambda cert, hostname: True
ssl._create_default_https_context = ssl._create_unverified_context

urlTxt = open("D:/haheehoData/urlList.txt", "r", encoding="utf-8") 
imgWordTxt = open("D:/haheehoData/imgWord.txt", "a", encoding="utf-8")

def getMainFrameSrc(url):
    global header
    req = requests.get(url, headers=header)
    bs = BeautifulSoup(req.text, "html.parser")
    realAddr = bs.select('#mainFrame')[0]["src"]
    
    return realAddr


def getMainContainer(realAddr):
    global header
    mainContainer = None
    req = requests.get("https://blog.naver.com%s" % realAddr, headers=header)
    bs = BeautifulSoup(req.text, "html.parser")
    try:
        mainContainer = bs.select(".se-main-container")[0]
    except:
        mainContainer = bs.select("#postViewArea")[0]
    
    return mainContainer
  
  
def getImgSrc(mainContainer):
    images = mainContainer.findAll("img")
    
    srcList = []
    
    for no, i in enumerate(reversed(images)):
        if no == 3:
            break
        srcList.append(i["src"])
    
    return srcList


pt.pytesseract.tesseract_cmd, sentence, src, s = None, None, None, None
urlT = urlTxt.readlines()

for no, url in enumerate(urlT):
    url = url.replace("\n", "")
    src = getImgSrc(getMainContainer(getMainFrameSrc(url)))
            
    for s in src:
        req = urllib.request.Request(s, headers= header)
        res = urllib.request.urlopen(req).read()
        pt.pytesseract.tesseract_cmd = R'C:\Program Files\Tesseract-OCR\tesseract'
        sentence = pt.image_to_string(Image.open(BytesIO(res)), lang='kor').replace("\n", "").replace("", "").replace("\t", "").replace(" ", "")
        print(sentence)
        imgWordTxt.write("%s\n" % sentence)
                
    print(no)
            
imgWordTxt.close()
urlTxt.close()
print(time.time() - start)