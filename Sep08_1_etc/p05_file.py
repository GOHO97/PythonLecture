# -*- coding:utf-8 -*-

f = open("D:/vsc/0908.txt", "r", encoding="utf-8")


for line in f.readlines():
    print(line)

f.close()