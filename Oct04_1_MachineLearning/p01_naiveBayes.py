# -*- coding:utf-8 -*-
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

trainData = ["진원이 형의 응애 하는 재채기 소리 너무 귀여워서 죽이고 싶어.", "배가 너무 고파 근데 똥도 마려워 어떡해?", "떡순튀 맛있겠다.", "살 빼야 되는데", "인천최고 귀요미 서영덕", "마무리는 역시 서영덕"]
label = ["호의", "욕구", "욕구", "걱정", "호의", "호의"]

cv = CountVectorizer()
cvResult = cv.fit_transform(trainData)
#print(cv.get_feature_names())
#print(cv.vocabulary_)
cvResult = cvResult.toarray()

mnb = MultinomialNB()
mnbAi = mnb.fit(cvResult, label)
#학습 시키고

sentence = [input("뭐 : ")]
#입력받고
sentenceCvResult = cv.transform(sentence)
#정규화
sentenceCvResult = sentenceCvResult.toarray()
#toarray()로 바꿔준다.
print(sentenceCvResult)
# 프린트 해보면 [[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]] 이렇게 나오는데 위에 학습시켜놓은 문장의 단어들 중 겹치는게 없어서 그럼.
result = mnbAi.predict(sentenceCvResult)
print(result[0])
# 라벨링 시켜놓은 것 중 뭔지 예측.

