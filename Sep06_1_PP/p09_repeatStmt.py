# -*- coding:utf-8 -*-
jEnd = False
for i in range(6):
    for j in range(6):
        if j == 3:
            jEnd = True
            break
        print(i, j)
    if jEnd:
        break

