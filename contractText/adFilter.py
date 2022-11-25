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
    mainContainer = bs.select(".se-main-container")[0]
    
    return mainContainer
  
  
def getImgSrcList(mainContainer, srcList):
    
    images = mainContainer.findAll("img")
    srcList = []
    no, i = None, None
    
    for no, i in enumerate(reversed(images)):
        if no == 3:
            break
        srcList.append(i["src"].replace("w80_blur", "w966"))
        
        
    return srcList


def isInCompanyList(srcList):
    # 가져온 srcList로 반복문을 돌려 3개 중에 companyList에 포함되어 있다면 바로 True return 셋다 없다면 False 리턴
    global companyList
    src = None
    
    for src in srcList:
        src = src.split("/")[2]
        if src in companyList:
            return  True
    
    return False


def isContainsImgKeyword(srcList):
    # 가져온 srcList로 반복문을 돌려 img에서 text를 추출하고 imgKeywordList에 포함되어 있다면 바로 True를 return 셋다 없다면 False 리턴
    global imgKeywordList, header
    pt.pytesseract.tesseract_cmd, src, sentence, ik = None, None, None, None
    req, res = None, None
    
    try:
        for src in srcList:
            req = urllib.request.Request(src, headers= header)
            res = urllib.request.urlopen(req).read()
            pt.pytesseract.tesseract_cmd = R'C:\Program Files\Tesseract-OCR\tesseract'
            sentence = pt.image_to_string(Image.open(BytesIO(res)).convert("L"), lang='kor')
            
            for ik in imgKeywordList:
                if sentence.__contains__(ik):
                    return True
    except Exception as e:
        exceptList.write("%s,%s,img요청 및 분석에서 터짐.\n" % (src, e))
    
    return False


def isContainsKeywordList(mainContainer):
    # 가져온 pList로 반복문을 돌려 text를 추출하고 keywordList에 포함 되어 있다면 바로 True를 return 셋 다 없다면 False 리턴
    global keywordList
    
    allP = mainContainer.select(".se-text-paragraph")
    p = None
    i = 0
    for p in reversed(allP):
        if i == 5:
            break
        if p.text != "\u200b" and p.text != " ":
            i += 1
            for kw in keywordList:
                if p.text.__contains__(kw):
                    return True
    return False
    

header = {"User-agent": "Mozilla/5.0"} 
ssl.match_hostname = lambda cert, hostname: True
ssl._create_default_https_context = ssl._create_unverified_context

urlTxt = open("D:/haheehoData/test.txt", "r", encoding="utf-8")
filterResult = open("D:/haheehoData/test2.txt", "a", encoding="utf-8")
exceptList = open("D:/haheehoData/exceptList.txt", "a", encoding="utf-8")
# 서버 구축 시 제거

companyList = ['www.revu.net', 'mateb.kr', 'www.storyn.kr', 'www.mrblog.net', 'xn--939au0g4vj8sq.net', 'dinnerqueen.net', 'reviewjin.com', 'www.ringble.co.kr', 'www.cometoplay.kr', 'realview.kr', 'echoblog.net', 'www.seoulouba.co.kr', 'www.99das.com', '4blog.net', 'www.reviewplace.co.kr', 'www.seoulouba.kr', 'jaview.co.kr', 'lipple.co.kr', 'www.modublog.co.kr', 'www.fineadple.com', 'bqueens.net', 'tqueens.net', 'www.pick-me.kr', 'www.tble.kr', 'leyongblog.com', 'www.witchad.kr', 'www.kormedia.co.kr', 'chehumdan.com', 'www.sioneview.com', 'www.powerblogs.kr', 'reviewshare.io', 'www.real-review.kr', 'www.reviewus.co.kr', 'nugunablog.co.kr', 'reviewtong.co.kr', 'www.sayblog.co.kr', 'blog.naver.com']
# 광고 회사 list
imgKeywordList = ['업체', '서비스', '식사권', '원고료', '소정', '받았지만', '받아', '받고', '포인트', '업제', '무상', '업처', '업세', '체험단', '광고주', '제작비', '이용권', '등록비', '원고류', '시비스', '수수료']
# 이미지 텍스트 추출 시 광고글의 키워드 list
keywordList = ['업체', '식사권', '원고료', '소정', '제공', '받았지만', '포인트', '무상', '광고주', '제작비', '이용권', '등록비', '수수료']
# p문단 텍스트 추출 시 광고글의 키워드 list

mainContainer, src, srcList = None, None, None
# html 요소들

urlT = urlTxt.readlines()

for no, url in enumerate(urlT):
    #if no == 3:
    #    break
    url = url.replace("\n", "")
    try:
        mainContainer = getMainContainer(getMainFrameSrc(url))
        # API에서 응답 받은 url에서 mainFrameSrc를 가져오고 해당 src로 재요청을 하여 mainContainer 객체를 가져온다.
    except Exception as e:
        exceptList.write("%d%s,%s,mainContainer에서 터짐\n" % (no, url, e))
        continue
        # except는 요청 과정에서 비공개글로 전환 했거나 mainContainer가 아닌 postViewArea가 있는 경우 등 너무 많은 변수가 있어 넘기기로 했다.
        # 실제 서버 구축 시 except에 continue가 아닌 들어온 요청에 "불가"와 같은 응답으로 대체해야 한다. 
    
    srcList = getImgSrcList(mainContainer, srcList)
    # 가져온 mainContainer에서 img 판독을 위한 srcList를 셋팅 해주는 함수를 부른다.
    
    if isInCompanyList(srcList):
        filterResult.write("%d,%s,CompanyList에서 걸림\n" % (no, url))
        # 실제 서버에선 광고 응답
    else :
        if isContainsImgKeyword(srcList):
            filterResult.write("%d,%s,imgKeyword에서 걸림\n" % (no, url))
            # 실제 서버에선 광고 응답
        else:
            if isContainsKeywordList(mainContainer):
                filterResult.write("%d,%s,textKeyword에서 걸림\n" % (no, url))
                # 실제 서버에선 광고 응답
            else:
                filterResult.write("%d,%s,광고 아님\n" % (no, url))
            
                
    print(no, "완료")
            
urlTxt.close()
filterResult.close()
exceptList.close()
print(time.time() - start)
# 서버 구축시 제거
