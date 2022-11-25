# -*- coding:utf-8 -*-
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet

ps = PorterStemmer()

d = "play playing played plays"

wt = word_tokenize(d)
for w in wt:
    print(w, ps.stem(w))
import nltk

wnl = WordNetLemmatizer()
d = "am are is"
wt = word_tokenize(d)
for w in wt:
    print(w, wnl.lemmatize(w, wordnet.VERB))