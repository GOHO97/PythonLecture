# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from json import loads
import pandas as pd
from sklearn.tree._classes import DecisionTreeClassifier
from sklearn.tree._export import export_graphviz

huc = HTTPConnection("openapi.seoul.go.kr:8088")
huc.request("GET", "/575a4655496b636839386f58586542/json/RealtimeCityAir/1/25")
rb = huc.getresponse().read()
dustData = loads(rb)["RealtimeCityAir"]["row"]
huc.close()
df = pd.DataFrame(dustData)
trainData = df[['PM10', 'PM25']].to_numpy()
label = df['IDEX_NM']

dtc = DecisionTreeClassifier()
dtc.fit(trainData, label)
cn = label.unique()
# unique로 뭐가 있는지 확인 해서 중복 빼기

export_graphviz(dtc, out_file='D:/img/dust.dot',
                class_names= cn, # 결과물들(라벨)
                feature_names=['PM10', 'PM25'], # 항목들
                filled=True, # 색칠할 것인지
                rounded=True # 모서리 깎을 것인지
                )
# 트리 같은 그래프 이미지가 필요한 것일테니 쓰는 것. (graphviz라는 프로그램에서 쓰는 파일로 내보내기.)
# graphviz에서 그림파일로 변환
print("끝")
