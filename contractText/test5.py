# -*- coding:utf-8 -*-
pKeywordTxt = open("D:/haheehoData/pKeyword.txt", "r", encoding="utf-8")
pKeywordTxt2 = open("D:/haheehoData/pKeyword2.txt", "a", encoding="utf-8")

a = pKeywordTxt.readlines()
for line in a:
    if not line == "\u200b\n":
        pKeywordTxt2.write(line)
        

pKeywordTxt.close()
pKeywordTxt2.close()