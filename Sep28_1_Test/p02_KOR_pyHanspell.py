# -*- coding:utf-8 -*-
from hanspell.spell_checker import check

d = '쌤 항상 감사합니다.. 또르륵 너무 맛있는거 제가 살라고했능데...은애가 신세가 많네요'

r = check(d)
print(r.checked)
print(r.errors)
print(r.words)

for w, r2 in r.words.items():
    print(w, r2)