# -*- coding:utf-8 -*-
from cx_Oracle import connect
import pandas as pd
from sklearn.tree._classes import DecisionTreeClassifier
from sklearn.tree._export import export_graphviz

db = connect("kwon/kwon@sdgn-djvemfu.tplinkdns.com:19195/xe")
df = pd.read_sql("select * from bnsaabfp_weather_color", db)
db.close()
weathers = list(df['BWC_WEATHER'].unique())
df['BWC_WEATHER'] = df['BWC_WEATHER'].apply(lambda d:weathers.index(d))

trainData = df[['BWC_HOUR', 'BWC_TEMP', 'BWC_HUMIDITY', 'BWC_WEATHER']].to_numpy()


dtc = DecisionTreeClassifier()
label = df["BWC_COLOR"]
dtc.fit(trainData, label)

cn = label.unique()

export_graphviz(dtc, out_file='D:/img/aiColor.dot',
                class_names= cn,
                feature_names=['BWC_HOUR', 'BWC_TEMP', 'BWC_HUMIDITY', 'BWC_WEATHER'],
                filled=True,
                rounded=True
                )
print('끝')
