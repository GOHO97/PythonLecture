# -*- coding:utf-8 -*-
import numpy as np

score = [[100, 90, 80], [80, 50, 40]]
print(type(score))
print(score)

score2 = np.array(score)
print(type(score2))
print(score2)

print(score[0][1])
print(score2[0][1])


print(score2.shape)
# 몇 행 몇 렬
print(score2.dtype)
# 자료형

print(len(score2))
print(score2.size)
# 총 몇개 들어있나
