# -*- coding:utf-8 -*-
from _operator import xor

name = input("이름 : ")
height = float(input("키 : "))
age = int(input("나이 : "))
print("----------")
print(name, height, age)

#나이가 5살 이상이면 "타", 아니면 "나가"
h = (age)