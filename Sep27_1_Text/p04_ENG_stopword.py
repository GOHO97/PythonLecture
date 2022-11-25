# -*- coding:utf-8 -*-
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize


# 불용어(stopword)
# 별 영양가 없는 것들 (a, the is 등등)
sw = stopwords.words("english")
d = "My mother and father is gentleman so I was happy umm.. How are you?"

wt = word_tokenize(d)

word = []
for w in wt:
    w = w.lower()
    if w not in sw:
        word.append(w)

print(word)