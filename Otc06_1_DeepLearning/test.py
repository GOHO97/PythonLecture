# -*- coding:utf-8 -*-
# https://blog.naver.com/minggu41/222851396311

from bs4 import BeautifulSoup
import requests
#https://blog.naver.com/hyewon1925/222596876179

url = "https://blog.naver.com/minggu41/222851396311"
req = requests.get(url, headers={"User-agent": "Mozilla/5.0"})
bs = BeautifulSoup(req.text, "html.parser")
realAddr = bs.select('#mainFrame')[0]["src"]
# 응답 받는 블로그 주소로 iframe 객체의 src 값을 가져온다.

req = requests.get("https://blog.naver.com" + realAddr, headers={"User-agent": "Mozilla/5.0"})
bs = BeautifulSoup(req.text, "html.parser")
images = bs.select(".se-main-container")[0].findAll("img")

companyList = ["www.revu.net", "www.seoulouba.co.kr", "modublog.co.kr", "www.ringble.co.kr", "xn--939au0g4vj8sq.net"]
# 광고 회사 리스트

src = []
for img in images:
    src.append(img["src"].split("/")[2])

# main-container에 들어있는 모든 img의 src 값을 /로 split 해주고 2번째 것의 값만 리스트에 담아준다.

for no, s in enumerate(reversed(src)):
    if no == 3:
        # 뒤에서 3번째 것 까지만 검사
        break
    print(s)
    if s in companyList:
        print("광고")
        # 여기서 끊고 요청에 응답 해주는 형식으로 만들 것이다.
        
