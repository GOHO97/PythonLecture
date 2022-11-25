# -*- coding:utf-8 -*-
def test():
    pass
def getHab(a, b):
    c = a + b
    return c 

def getCalcResult(a, b):
    c = a + b
    d = a - b
    e = a * b
    f = a / b
    return (c,d,e,f)

q = getCalcResult(100, 50)
print(q, type(q))

