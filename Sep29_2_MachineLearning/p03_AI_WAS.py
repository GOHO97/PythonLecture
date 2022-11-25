# -*- coding:utf-8 -*-
# kwon/kwon@sdgn-djvemfu.tplinkdns.com:19195/xe
# bnsaabfp_weather_color
from cx_Oracle import connect
import pandas as pd
from sklearn.preprocessing._data import MinMaxScaler
import numpy as np
from sklearn.neighbors._classification import KNeighborsClassifier
from http.client import HTTPSConnection
from json import loads
from _datetime import datetime
from flask.app import Flask
from flask import request
from flask.json import jsonify
from flask.helpers import make_response

mms = MinMaxScaler()
knc = KNeighborsClassifier(10)
weathers = None
day = -1


def trainAI():
    global mms, knc, weathers
    
    db = connect("kwon/kwon@sdgn-djvemfu.tplinkdns.com:19195/xe")
    df = pd.read_sql("select * from bnsaabfp_weather_color", db)
    db.close()
    # 다른건 숫자라 labeling 하기 괜찮지만 날씨는 한글이라 조치가 필요함.
    weathers = list(df['BWC_WEATHER'].unique())
    # ['튼구름' '구름조금' '실 비' '맑음' '온흐림' '보통 비'] 이렇게 list 형태임.
    # 만약 날씨가 흐림 - 맑음에 따라 숫자가 정비례 하게끔 하고 싶다면 배열을 따로 만드는 것이 좋을 것이다.
    df['BWC_WEATHER'] = df['BWC_WEATHER'].apply(lambda d:weathers.index(d))
    # 인덱스를 통해 기존 한글 데이터를 숫자로 바꿔줌.
    trainData = df[['BWC_HOUR', 'BWC_TEMP', 'BWC_HUMIDITY', 'BWC_WEATHER']].to_numpy()
    # numpy로 배열로 변경 해줌.
    label = df['BWC_COLOR']
    trainData = mms.fit_transform(trainData)
    knc.fit(trainData, label)
    

app = Flask(__name__)

def getWeatherData():
    global weathers
    huc = HTTPSConnection("api.openweathermap.org")
    huc.request("GET", "/data/2.5/weather?q=seoul&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr")
    resbody = huc.getresponse().read()
    weatherData = loads(resbody)
    
    w = None
    try :
        w = weathers.index(weatherData["weather"][0]["description"])
    except:
        w = -1
    
    h = datetime.today().hour
    t = weatherData["main"]["temp"]
    hu = weatherData["main"]["humidity"]
    
    return h, t, hu, w

@app.route("/color.get")
def getColor():
    global mms, knc,day
    today = datetime.today().day
    if day != today:
        trainAI()
        day = today
    h, t, hu, w = getWeatherData()
    userdata = np.array([[h, t, hu, w]])
    userdata = mms.transform(userdata)
    result = knc.predict(userdata)[0]
    result = {"color": result}
    
    return make_response(jsonify(result)), {"Access-control-Allow-Origin": "*"}

    
if __name__=="__main__":
    app.run("0.0.0.0", # 접속을 허용해줄 주소
            7887,       # 포트번호
            debug=True  # 콘솔에 로그
            )
