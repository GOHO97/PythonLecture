# -*- coding:utf-8 -*-
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tag import pos_tag
import pandas as pd

sw = stopwords.words("english") # 불용어들 저장된 배열
wnl = WordNetLemmatizer() # 동사 원형으로 만들어줄 객체
f = open("D:/csvdict/book.txt", "r", encoding="utf-8")
file = word_tokenize(f.read()) # 파일 전체를 단어 기준으로 잘라줌

words = {} # 숫자 세줄 dict
for f2 in file:
    f2 = f2.lower()
    if f2 not in sw: # 불용어, 특수문자 날리고
        f2, p = pos_tag([f2])[0] # 품사 태깅해서
        if p.startswith("V"): # 동사만
            f2 = wnl.lemmatize(f2, wordnet.VERB) # 표제어 추출
            if f2 in words:
                words[f2] += 1
            else:
                words[f2] = 1
f.close()

f3 = open("D:/csvdict/bookResult.csv", "a", encoding="utf-8")
df = []
for k, v in words.items():
    df.append({"단어" : k, "횟수" : v})
    f3.write("%s,%d\n" % (k, v))

f3.close()

df = pd.DataFrame(df)
df = df.sort_values(by=["횟수"], ascending=False)
df.to_csv("D:/csvdict/bookResult2.csv", index=False, header=False)

