# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
#https://blog.naver.com/hyewon1925/222596876179

url = "https://blog.naver.com/hyewon1925/222596876179"
req = requests.get(url, headers={"User-agent": "Mozilla/5.0"})
bs = BeautifulSoup(req.text, "html.parser")
realAddr = bs.select('#mainFrame')[0]["src"]
# 응답 받는 블로그 주소로 iframe 객체의 src 값을 가져온다.

req = requests.get("https://blog.naver.com" + realAddr, headers={"User-agent": "Mozilla/5.0"})
bs = BeautifulSoup(req.text, "html.parser")
mainContent = bs.select(".se-main-container")[0].text.replace("\n", "")

print(mainContent)

