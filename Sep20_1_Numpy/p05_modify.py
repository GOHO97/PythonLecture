# -*- coding:utf-8 -*-
import numpy as np

a = np.random.randint(1, 100, [3, 5])
print(a)

a[0, 1] = 20
print(a)

b = np.where(a % 2 == 1, 0, a)
print(b)