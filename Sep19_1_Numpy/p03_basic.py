# -*- coding:utf-8 -*-
import numpy as np

s = "ㅋ"
s2 = "ㅎ"

s3 = s + s2
print(s3)

a = [10, 20]
b = [1, 2]
c = a + b
print(c)

e = a * 3
print(e)

aa = np.array([10, 20])
bb = np.array([1, 2])
cc = aa + bb
print(cc)

dd = aa * bb
print(dd)

ee = aa * 3
print(ee)


name = np.array(["홍길동", "김길동", "이길동"])
kor = np.array([100, 80, 20])
eng = np.array([10, 83, 12])
mat = np.array([33, 42, 80])

avg = (kor + eng + mat) / 3
print(avg)
over40 = avg > 40
print(over40)

print(name[over40])
print(name[kor > 90])


print(name[(avg >= 40) & (avg <= 50)])




