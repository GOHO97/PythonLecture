# -*- coding:utf-8 -*-
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tag import pos_tag
from wordcloud.wordcloud import WordCloud
import matplotlib.pyplot as plt

sw = stopwords.words("english")
wnl = WordNetLemmatizer()
f = open("D:/csvdict/book.txt", "r", encoding="utf-8")

file = word_tokenize(f.read())
words = ""

for f2 in file:
    f2 = f2.lower()
    if f2 not in sw : # 불용어  날리고
        f2, p = pos_tag([f2])[0] # 품사 태깅해서
        if p.startswith("V"): # 동사만
            f2 = wnl.lemmatize(f2, wordnet.VERB) # 표제어 추출
            words += f2 + " "
f.close()

wc = WordCloud(font_path="C:/Windows/Fonts/malgun.ttf", background_color="white").generate(words)
plt.imshow(wc)
plt.show()


