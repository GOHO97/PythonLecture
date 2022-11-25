# -*- coding:utf-8 -*-
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

#import nltk
#nltk.download('averaged_perceptron_tagger')

d = "He was still, as ever, deeply attracted by the study of crime, and occupied his immense faculties and extraordinary powers of observation in following out those clues, and clearing up those mysteries which had been abandoned as hopeless by the official police."
wt = word_tokenize(d)
wt = pos_tag(wt)
# 품사 태깅해서 튜플로 반환 함.
for w, t in wt:
    print(w, t)

