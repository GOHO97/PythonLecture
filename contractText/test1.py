# -*- coding:utf-8 -*-
# https://blog.naver.com/minggu41/222851396311

from bs4 import BeautifulSoup
import requests
#https://blog.naver.com/hyewon1925/222596876179

header = {"User-agent": "Mozilla/5.0"} 

url = "https://blog.naver.com/violetdevil3/222688201868"
req = requests.get(url, headers=header)
bs = BeautifulSoup(req.text, "html.parser")
realAddr = bs.select('#mainFrame')[0]["src"]
# 응답 받는 블로그 주소로 iframe 객체의 src 값을 가져온다.

req = requests.get("https://blog.naver.com" + realAddr, headers=header)
bs = BeautifulSoup(req.text, "html.parser")
mainContainer = bs.select(".se-main-container")[0]
# blog content의 메인 객체

images = mainContainer.findAll("img")
# 이미지 만을 담아준다.

sentence = bs.select(".se-text-paragraph")

for s in sentence:
    print(s.text.replace("\n", ""))    
