# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from json import loads
import pandas as pd
import tensorflow as tf


huc = HTTPConnection("openapi.seoul.go.kr:8088")
huc.request("GET", "/575a4655496b636839386f58586542/json/RealtimeCityAir/1/25")
rb = huc.getresponse().read()
dustData = loads(rb)["RealtimeCityAir"]["row"]
huc.close()
df = pd.DataFrame(dustData)

xData = df['PM10'].to_numpy()
yData = df['PM25'].to_numpy()

a = tf.Variable(tf.zeros([1], tf.float64))
b = tf.Variable(tf.zeros([1], tf.float64))
# 이게 사실 첫 값이라 그냥 이런식으로 0 들어가도 상관 없는데
# 왠진 모르겠지만 다른 모든 사람들이 아까 그것 처럼 한단다.

x = tf.placeholder(tf.float64)
y = tf.placeholder(tf.float64)

sik = a * x + b

distance = tf.reduce_mean(tf.square(y - sik))
ao = tf.train.AdamOptimizer(learning_rate=0.001)
goal = ao.minimize(distance)

s = tf.Session()
s.run(tf.global_variables_initializer())

while True:
    s.run(goal, {x:xData, y:yData})
    print("y = %fx + %f" % (s.run(a), s.run(b)))
    d = s.run(distance, {x:xData, y:yData})
    print(d)
    print("-----")
    
    if d < 2.714:
        break
    
newX = float(input("x : "))
result = s.run(sik, {x:newX})
print(result)


