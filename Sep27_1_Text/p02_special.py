# -*- coding:utf-8 -*-
from sys import maxunicode
from unicodedata import category

print(maxunicode) # ubicode 전체 수
print(chr(99)) # index번째 글자
print(category('a')) # 들어있는 글자의 종류가 뭔지 알려준다.
print("----")
specials = []
for i in range(maxunicode):
    if category(chr(i)).startswith("P"): #P로 시작하는 애들이 특수문자
        specials.append(chr(i))
        
