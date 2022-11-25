# -*- coding:utf-8 -*-
import numpy as np

a = np.random.randint(1, 21, [10])
b = np.random.randint(1, 21, [10])
print(a)
print(b)

c = np.intersect1d(a, b) # 교집합
print(c)

d = np.union1d(a, b) # 합집합
print(d)

e = np.setdiff1d(a, b) # 차집합(a에서 b에 있는거 빼고)
print(e)

f = np.setxor1d(a, b) # a등 b든 한쪽에만 있는 거
print(f)

g = np.unique(a) # 중복제거
print(g)