# -*- coding:utf-8 -*-
from jamo.jamo import h2j, j2hcj
from unicode import join_jamos

d = "똥"
r = h2j(d)
print(r)

r2 = j2hcj(r)
print(r2)

r3 = join_jamos(d)
print(r3)