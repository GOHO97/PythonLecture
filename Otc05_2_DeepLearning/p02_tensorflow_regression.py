# -*- coding:utf-8 -*-
import tensorflow as tf

xData = [1, 2, 3]
yData = [12, 22, 32]
# x, y로 쓸 값

# 첫 값 지정
a = tf.Variable(tf.random_uniform([1], # 차원지정
                                   -2, 3, # -2 ~ 3사이의 랜덤[정규 분포]
                                    tf.float64 # 자료형
                                    ))
# b도 마찬가지
b = tf.Variable(tf.random_uniform([1], # 차원지정
                                   -2, 3, # -2 ~ 3사이의 랜덤[정규 분포]
                                    tf.float64 # 자료형
                                    ))

# a와 b는 컴퓨터가 찾아내야할 값이라 위 처럼 설정을 좀 상세하게 해주고
x = tf.placeholder(tf.float64)
y = tf.placeholder(tf.float64)
# x, y는 어차피 우리가 넣을 것이니 이정도로만 해준다.

sik = a * x + b
# 라는 식에 대입해서 나온다면 대충 sik = 2.123x + -1.51 이런식으로 나올 것이다.
# 위 식에 x가 1이면 y는 0.613인데 실제로는 x가 1일 때 y는 10이다.
# 위와 같은 오차를 줄여나가는 것이 목표이며 sik을 통해 구한 y값과 실제 y값과의 오차가 적으면 식을 잘 찾았다는 말이다.

distance = tf.reduce_mean(tf.square(y - sik))
# 차원 수를 줄이고, 평균을 구한다.

ao = tf.train.AdamOptimizer(learning_rate=0.001)
# 최적의 a, b를 찾아줄 객체

# learning_rate는 값을 크게도 작게도 가능하다.
# 값 크게 : 두번째 회차 부터의 a, b를 찾을 때 값이 넓어지는 범위가 좀 더 커진다. 또한 올라가는 숫자가 큰 만틈 속도가 빠르며 자칫하면 답을 못찾을 수도 있다.
# 값 작게 : 위와는 반대로 흘러간다. 느리지만 답은 확실히 찾아진다.
# learning_rate를 얼마나 적절하게 설정하냐가 중요 포인트다.

goal = ao.minimize(distance)
# 위에서 설정한 목표 y와 sik의 거리가 줄어드는 것이 목표라는 것을 알려준다.

# 2) 학습데이터 넣어서 최적의 알고리즘 찾기
s = tf.Session()
s.run(tf.global_variables_initializer())
# tf.variable들 초기화

while True:
    s.run(goal, {x:xData, y:yData})
    # 각각의 placeholder에 값 넣어준다.
    print("y = %fx + %f" % (s.run(a), s.run(b)))
    # a 값, b 값 보고 싶어서 
    d = s.run(distance, {x:xData, y:yData})
    print(d)
    print("-----")
    
    if d == 0:
        break
    
newX = float(input("x : "))
result = s.run(sik, {x:newX})
print(result)
