# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests

save1 = []
url = "https://blog.naver.com/PostView.naver?blogId=syo818&logNo=222628076485&redirect=Dlog&widgetTypeCall=true&topReferer=https%3A%2F%2Fsearch.naver.com%2Fsearch.naver%3Fwhere%3Dview%26sm%3Dtab_jum%26query%3D%25EA%25B0%2595%25EB%2582%25A8%25EC%2597%25AD%2B%25EB%25A7%259B%25EC%25A7%2591&directAccess=false"
req = requests.get(url, headers={'User-agent': 'Mozilla/5.0', "directAccess": "true"})

data = BeautifulSoup(req.text, "lxml")
data2 = data.find_all("div", {"class": "se-main-container"})

for title in data2:
    save1.append(title.get_text())

print(save1)
