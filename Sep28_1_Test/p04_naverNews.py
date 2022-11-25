# -*- coding:utf-8 -*-
from hanspell.spell_checker import check
from konlpy.tag._okt import Okt
import pandas as pd

f = open("D:/csvdict/metaversData/kakaoBlogData.csv", "r", encoding="utf-8")

line = None
data = ""
o = Okt()
d = {}
for line in f.readlines():
    try:
        line = check(line).checked # 맞춤법검사
        line = o.normalize(line) # 정규화
        for w, p in o.pos(line, stem=True):
            if p == "Noun": # 명사면
                if w in d:
                    d[w] += 1
                else:
                    d[w] = 1
    except:
        pass
f.close()

l = []
for k, v in d.items():
    l.append({"단어": k, "횟수" : v})
df = pd.DataFrame(l)
df = df.sort_values(by="횟수", ascending=False)
print(df)