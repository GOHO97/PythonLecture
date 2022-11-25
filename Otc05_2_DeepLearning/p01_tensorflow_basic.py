# -*- coding:utf-8 -*-
import tensorflow as tf

# 1) 인공신경망 구성
a = tf.constant(23)
b = tf.constant(34)
c = tf.add(a, b)
print(a)

d = tf.constant("ㅋ")

# 2) 학습 데이터 넣어서 최적의 알고리즘 찾고
s = tf.Session() # 실행 세션
cResult = s.run(c) # 그 세션으로 돌리는 것.
# 실행 하면 그 때서야 값이 들어간다.
print(cResult)
dResult = s.run(d)
print(dResult)



# 3) 예측
