# -*- coding:utf-8 -*-
from hanspell.spell_checker import check
from konlpy.tag._okt import Okt
import pandas as pd

f = open("D:/csvdict/sam2Result.txt", "r", encoding="utf-8")
o = Okt()
d = {}
for line in f.readlines():
    try:
        word = line.split("\t")[0]
        word = check(word).checked
        word = o.normalize(word)
        for w, p in o.pos(word, stem=True):
            if p == "Verb":
                if w in d:
                    d[w] += 1
                else:
                    d[w] = 1
        print(word)
    except:
        pass
f.close()

f2 = open("D:/csvdict/sam2Result2.csv", "a", encoding="utf-8")

for k, v in d.items():
    f2.write("%s,%d\n" % (k, v))

f2.close()
