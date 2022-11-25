# -*- coding:utf-8 -*-
import numpy as np

a = np.zeros([3, 2])
print(a)

b = np.ones([3, 2])
print(b)

c = np.empty([3, 2])
print(c)

d = np.arange(5)
print(d)

g = np.random.rand(3, 2)
print(g)

h = np.random.randn(3, 2)
print(h)

i = np.random.randint(1, 20, [3, 2])
print(i)