# -*- coding:utf-8 -*-
from _datetime import datetime
from time import strftime

ss = "2022/12/31"
d2 = datetime.strptime(ss, '%Y/%m/%d')
s2 = datetime.strftime(d2, "%Y-%m-%d")

print(d2)
print(s2)

myBirthday = "1997/07/20" 
myBirthDate = datetime.strptime(myBirthday, "%Y/%m/%d")
myBirthdayWeekday = datetime.strftime(myBirthDate, "%A")
print(myBirthdayWeekday)