# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from urllib.parse import quote
from json import loads

what = input("뭐 : ")
what2 = quote(what)
h = {"Authorization": "KakaoAK f97c35a2dec2c919adebacba62e5bae2"}
hc = HTTPConnection("dapi.kakao.com")
hc.request("GET", "/v2/local/search/keyword.json?x=127.026669&y=37.505377&radius=1000&query="+what2, headers=h)
rb = hc.getresponse().read()
hc.close()

f = open("D:/csvdict/kakaoData/loc.txt", "a", encoding="utf-8")

for l in loads(rb)["documents"]:
    f.write("%s\t%s\t%s\t%s\n" % (
        l['place_name'],
        what,
        l['y'],
        l['x']
        ))
f.close()