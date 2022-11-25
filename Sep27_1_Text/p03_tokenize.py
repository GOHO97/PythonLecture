# -*- coding:utf-8 -*-
import nltk # 다운을 미리 받아 놓고 하는 것
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download("punkt")# 특수문자들

d = "몽둥이 금지라구요??? 당연한 말씀 그럼 방망이? 몽둥이, 회초리, 방망이 매 막대기"
#wt = word_tokenize(d)
#print(wt)

st = sent_tokenize(d)
print(st)