# -*- coding:utf-8 -*-
import numpy as np
from sklearn.neighbors._classification import KNeighborsClassifier

data = np.array([[80, 20], [95, 5], [10, 90], [90, 10], [5, 95]])
label = np.array(['액션', '액션', '조폭', '액션', '조폭'])

knc = KNeighborsClassifier(3) # 가장 가까운거 k개 뽑기, k = ? 
knc.fit(data, label) # 학습 시키기

a = float(input("격투 : "))
b = float(input("욕 : "))
myData = np.array([[a, b]])
result = knc.predict(myData) # 예측 시키기
print(result[0])
