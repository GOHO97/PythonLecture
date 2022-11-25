# -*- coding:utf-8 -*-
import numpy as np

a = np.random.randint(1, 51, [3, 5])
print(a)
print("---------")
b = np.sort(a)
print(b)
print("---------")

c = np.sort(a, axis=0)
print(c)
print("---------")

e = np.sort(a, axis=0)[::-1]
print(e)
print("---------")

f = np.sort(a)[::-1]
print(f)
print("---------")

aa = []
for row in a:
    aa.append(np.sort(row)[::-1])
aa = np.array(aa)
print(aa)