# -*- coding:utf-8 -*-
import tensorflow as tf

xData = [[80, 20], [95, 5], [10, 90], [90, 10], [5, 95]]
yData = [[1, 0], [1, 0], [0, 1], [1, 0], [0, 1]]
label = ['액션', '조폭']

# xData : (1 x 2)
a = tf.Variable(tf.zeros([len(xData[0]), len(yData[0])], tf.float64))
b = tf.Variable(tf.zeros([len(yData[0])], tf.float64))

x = tf.placeholder(tf.float64)
y = tf.placeholder(tf.float64)

sik = tf.add(tf.matmul(x, a), b)

distance = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=y, logits=sik))

ao = tf.train.AdamOptimizer(learning_rate=0.01)
goal = ao.minimize(distance)

s = tf.Session()
s.run(tf.global_variables_initializer())

while True:
    s.run(goal, {x:xData, y:yData})
    d = s.run(distance, {x:xData, y:yData})
    print(s.run(a), s.run(b))
    print(d)
    if d < 0.01:
        break
    
a = float(input("싸움 : "))
b = float(input("욕 : "))
newMovie = [[a, b]] 
result = s.run(tf.argmax(sik, 1), {x:newMovie})
print(label[result[0]])