# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
from PIL import Image
import urllib.request
from io import BytesIO
import pytesseract as pt
import ssl

header = {"User-agent": "Mozilla/5.0"} 
ssl.match_hostname = lambda cert, hostname: True
ssl._create_default_https_context = ssl._create_unverified_context

imgKeywordList = ['업체', '서비스', '식사권', '원고료', '소정의', '받았지만', '받아', '받고', '포인트', '업제', '무상', '업처', '업세', '광고주', '제작비', '이용권', '등록비', '원고류', '시비스', '수수료']
# 이미지 텍스트 추출 시 광고글의 키워드 list

s = "https://postfiles.pstatic.net/MjAyMjEwMTdfNiAg/MDAxNjY1OTkyODgyNjkz.FzHoiISEYhJmoZRkbHMfLQmImiDZFnUlI3kOIhwwYsMg.MiR3Htc5dh5fhK-NDN3GqINOaiDDOyIRgx67mwAi_yog.JPEG.peachbath/1665992880353.jpg?type=w580"
req = urllib.request.Request(s, headers= header)
res = urllib.request.urlopen(req).read()
foreground = Image.open(BytesIO(res))
backImg = Image.open("D:/haheehoData/whiteBoard.png")
pt.pytesseract.tesseract_cmd = R'C:\Program Files\Tesseract-OCR\tesseract'
sentence = pt.image_to_string(Image.alpha_composite(foreground, backImg), lang='kor')
print(sentence)

for ik in imgKeywordList:
    if sentence.__contains__(ik):
        print("광고")

# https://postfiles.pstatic.net/MjAyMjEwMDRfMjA5/MDAxNjY0ODQ3Mzg0NDg3.zOM2dso-fzNb5cMHwuFcbH5lZLg7gCYwdzSmR4vttGYg.C5rgVpB4UehtrhJqBjK_nx8LRr5NB95vyjZOk_oMd4Ag.JPEG.syaysa1/187900_footer.jpg?type=w966
# https://postfiles.pstatic.net/MjAyMjEwMDRfMjA5/MDAxNjY0ODQ3Mzg0NDg3.zOM2dso-fzNb5cMHwuFcbH5lZLg7gCYwdzSmR4vttGYg.C5rgVpB4UehtrhJqBjK_nx8LRr5NB95vyjZOk_oMd4Ag.JPEG.syaysa1/187900_footer.jpg?type=w966