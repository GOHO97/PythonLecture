# -*- coding:utf-8 -*-
d = 100
e = 200

def test(a, b, c):
    print(a, b[0], c[0], d, e)
    a = 20; b[0] = 100; c = [10, 20]; d = 200; e = 100
    print(a, b[0], c[0])

a = 10; b = [10, 20]; c = [100, 200]
print(a, b[0], c[0])
test(a, b, c)
print(a, b[0], c[0])