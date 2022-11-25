# -*- coding:utf-8 -*-
import numpy as np

a = np.random.randint(1, 101, [3, 5])
b = np.random.randint(1, 101, [3, 5])
print(a)
print(b)

c = np.concatenate([a, b])
print(c)

d = np.append(a, b)
print(d)

f = np.append(a, b, axis = 0)
print(f)

h = np.array_split(a, 2)
print()

i = np.split(a, 3)
print(i)