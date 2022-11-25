# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
from PIL import Image
import urllib.request
from io import BytesIO
import pytesseract as pt

header = {"User-agent": "Mozilla/5.0"} 
url = "https://blog.naver.com/violetdevil3/222688201868"

req = requests.get(url, headers=header)
bs = BeautifulSoup(req.text, "html.parser")
realAddr = bs.select('#mainFrame')[0]["src"]
# 네이버 API에서 응답 받는 블로그 주소로 iframe 객체의 src 값을 가져온다.

req = requests.get("https://blog.naver.com" + realAddr, headers=header)
# 블로그 컨텐츠 객체를 가져올 수 있는 실제 주소로 재요청 
bs = BeautifulSoup(req.text, "html.parser")

mainContainer = bs.select(".se-main-container")[0]
# blog content의 메인 객체
images = mainContainer.findAll("img")
# 검사용 이미지 만을 담아준다.


companyList = ["www.revu.net", "www.seoulouba.co.kr", "modublog.co.kr", "www.ringble.co.kr", "xn--939au0g4vj8sq.net"]
# 광고 회사 리스트
wordList = ["업체", "소정의", "서비스", "원고료", "식사권"]
# 광고 키워드 리스트


srcList = []
# imges 아이템들 중 뒤에서 3번째 까지만 담아 놓을 list
src, no, img, res, imgText, s, wl, sl = None, None, None, None, None, None, None, None
# 반복문에 들어가는 변수들

for no, img in enumerate(reversed(images)):
    if no == 3:
        break
    # 3번까지만 반복
    src = img["src"]
    srcList.append(src)
    
    if src.split("/")[2] in companyList:
        print('광고')
        break

pt.pytesseract.tesseract_cmd, str1 = None, None

for sl in srcList:
    req = urllib.request.Request(sl, headers= header)
    res = urllib.request.urlopen(req).read()
    pt.pytesseract.tesseract_cmd = R'C:\Program Files\Tesseract-OCR\tesseract'
    str1 = pt.image_to_string(Image.open(BytesIO(res)), lang='kor').replace("\n", "")
    for wl in wordList:
        if str1.__contains__(wl):
            print(str1)
            print("광고")

sentence = bs.select(".se-text-paragraph")
# mainContainer안의 문장을 쓸 때 생성되는 p객체의 class를 select하여 가져옴.

for no, s in enumerate(reversed(sentence)):
    if no == 3:
        break
    # 3번까지만 반복
    for wl in wordList:
        if s.text.__contains__(wl):
            print("광고")
            break
