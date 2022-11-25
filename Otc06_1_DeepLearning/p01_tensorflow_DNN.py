# -*- coding:utf-8 -*-
import tensorflow as tf

xData = [[80, 20], [95, 5], [10, 90], [90, 10], [5, 95]]
yData = [[1, 0], [1, 0], [0, 1], [1, 0], [0, 1]]
label = ['액션', '조폭']

x = tf.placeholder(tf.float64)
y = tf.placeholder(tf.float64)

a1 = tf.Variable(tf.zeros([len(xData[0]), 100], tf.float64))
b1 = tf.Variable(tf.zeros([100], tf.float64))
sik1 = tf.add(tf.matmul(x, a1), b1)

a2 = tf.Variable(tf.zeros([100, 50], tf.float64))
b2 = tf.Variable(tf.zeros([50], tf.float64))
sik2 = tf.add(tf.matmul(sik1, a2), b2)

a3 = tf.Variable(tf.zeros([50, 200], tf.float64))
b3 = tf.Variable(tf.zeros([200], tf.float64))
sik3 = tf.add(tf.matmul(sik2, a3), b3)

a4 = tf.Variable(tf.zeros([200, len(yData[0])], tf.float64))
b4 = tf.Variable(tf.zeros(len(yData[0]), tf.float64))
sik4 = tf.add(tf.matmul(sik3, a4), b4)
# 위 처럼 어떤 식으로 몇개의 결과를 도출 해내는 층을 여러개 만드는 것인데
# 황성화 함수 : 전기의 흐름을 묘사하는 중인데 값이 너무 작은거는 전기가 안 흐른걸로 취급해서 다음 층 계산할 때 제외 시키는 작업이다.
# 위 처럼 하면 작업이 일단 빨리질 것이고 relu : 값이 음수면 0으로 그냥 바꿔버린다.
# 아무튼 이 인공신경망의 정체는 그냥 다차원, 다층 회귀분석이다.

distance = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=y, logits=sik4))

ao = tf.train.AdamOptimizer(learning_rate=0.0001)
goal = ao.minimize(distance)

s = tf.Session()
s.run(tf.global_variables_initializer())

while True:
    s.run(goal, {x:xData, y:yData})
    d = s.run(distance, {x:xData, y:yData})
    print(d)
    if d < 0.674:
        break
    
a = float(input("싸움 : "))
b = float(input("욕 : "))
newMovie = [[a, b]] 
result = s.run(tf.argmax(sik4, 1), {x:newMovie})
print(label[result[0]])
