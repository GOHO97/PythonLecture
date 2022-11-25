# -*- coding:utf-8 -*-
from flask.app import Flask
from flask import request
from flask.json import jsonify
from flask.helpers import make_response
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

app = Flask(__name__)

@app.route("/ai.service")
def ai():
    airplane = request.args.get("airplane")
    game = request.args.get("game")
    ice = request.args.get("ice")
    predictData = np.array([[airplane, game, ice]])
    predictData = mms.transform(predictData)
    result = knc.predict(predictData)[0]
    result = {"결과": result}
    
    return make_response(jsonify(result)), {"Access-control-Allow-Origin": "*"}

    
if __name__=="__main__":
    app.run("0.0.0.0", # 접속을 허용해줄 주소
            7887,       # 포트번호
            debug=True  # 콘솔에 로그
            )

