# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.preprocessing._data import MinMaxScaler
from sklearn.neighbors._classification import KNeighborsClassifier

df = pd.read_csv("D:/csvdict/datingTestSet.txt", sep="\t", names=['비행기', '게임', '아이스크림', '인기'])

trainData = df[['비행기', '게임', '아이스크림']].to_numpy()
label = df['인기'].to_numpy()

mms = MinMaxScaler() # 최대 최소 구해서 정규화 처리 해줄 객체
trainData = mms.fit_transform(trainData) # 정규화 처리

# x, y, z축 => 유클리드 거리로 계산
knc = KNeighborsClassifier(20)
knc.fit(trainData, label)

# fit은 기준 삼을 데이터 넣어주는 것 transform은 판정 받을 값 넣는 것.
air = float(input("비행기 : "))
game = float(input("게임 : "))
ice = float(input("아이스크림 : "))
predictData = np.array([[air, game, ice]]) # 배열 만들고
predictData = mms.transform(predictData) # 배열 정규화 처리
result = knc.predict(predictData) # 결과 판정
print(result[0], type(result[0]))
