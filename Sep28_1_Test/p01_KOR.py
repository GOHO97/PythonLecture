# -*- coding:utf-8 -*-
from konlpy.tag._okt import Okt

d = "면접이랑 코테 준비 팁좀요 빨리 은행 가서 현금 찾으셔야겠넼ㅋㅋㅋㅋ 편한 복장"

o = Okt() # Open Korean Text 분석기(구] 트위터 한글 형태소 분석기)


dd = "몽둥이가 필요하겠네ㅋㅋㅋㅋㅋ"
#초성, 중성, 종성 때문에 오타가 더 많이 날 수 밖에 없음
# 그래서 위 같은 정규화(정리)가 있음
r = o.normalize(d)
print(r)
r = o.phrases(d)
print(r)
r = o.morphs(d)
print(r)
r = o.morphs(d, stem=True)
print(r)
r = o.pos(d) 
# 형태소 분석(단어, 품사) tuple 형태로
for w, p in r:
    print(w, p)

r = o.pos(d, join=True)
# 형태소 분석 -> 단어/품사 str 형태로
for w in r:
    print(w)
    
r = o.pos(d, stem=True)
for w, p in r:
    print(w, p)
    
r = o.nouns(d)
for w in r:
    print(w)