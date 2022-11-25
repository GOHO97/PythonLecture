# -*- coding:utf-8 -*-
import tensorflow as tf
import os
import cv2

def getImg(folder, w, h):
    datas =[]
    for f in os.listdir(folder): #폴더 속에 있는 파일명들
        data = cv2.imread(folder + "/" + f, cv2.IMREAD_GRAYSCALE)
        data = cv2.resize(data, (w, h))
        data = data.flatten() # 2차원(50 X 100) -> 1차원(5000)
        # 한줄로 펼쳐 준다.
        datas.append(data)
    
    return datas
    
xData = getImg("C:/Users/sundooedu/Desktop/mineral/hero", 100, 50)
yData = [0,0,0,0,0, 1,1,1,1,1, 2,2,2,2,2, 3,3,3,3,3, 4,4,4,4,4, 5,5,5,5,5]
# 갯수 한정적이고 순서대로 파일이 있어서 라벨링 이렇게 해줌 그냥
label = ['아이언맨', '스파이더맨', '배트맨', '졸라맨', '손오공', '배지터']

x = tf.placeholder(tf.float64)
y = tf.placeholder(tf.float64)

a1 = tf.Variable(tf.random_uniform([len(xData[0]), 1000], -1, 1, tf.float64))
b1 = tf.Variable(tf.zeros([1000], tf.float64))
sik1 = tf.add(tf.matmul(x, a1), b1)

a2 = tf.Variable(tf.random_uniform([1000, 1000], -1, 1, tf.float64))
b2 = tf.Variable(tf.zeros([1000], tf.float64))
sik2 = tf.add(tf.matmul(sik1, a2), b2)

a3 = tf.Variable(tf.random_uniform([1000, 1000], -1, 1, tf.float64))
b3 = tf.Variable(tf.zeros([1000], tf.float64))
sik3 = tf.add(tf.matmul(sik2, a3), b3)

a4 = tf.Variable(tf.random_uniform([1000, len(label)], -1, 1, tf.float64))
b4 = tf.Variable(tf.zeros(len(label), tf.float64))
sik4 = tf.add(tf.matmul(sik3, a4), b4)

distance = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=y, logits=sik4))

ao = tf.train.AdamOptimizer(learning_rate=0.0001)
goal = ao.minimize(distance)

s = tf.Session()
s.run(tf.global_variables_initializer())

print(yData)
yData = s.run(tf.one_hot(yData, 6))


for _ in range(1000):
    s.run(goal, {x:xData, y:yData})
    d = s.run(distance, {x:xData, y:yData})
    print(d)
    if d < 0.001:
        break

while True:
    f = input("경로 : ")    
    f = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
    f = cv2.resize(f, (100, 50))
    f = [f.flatten()]
    result = s.run(tf.argmax(sik4, 1), {x:f})
    print(label[result[0]])
    

