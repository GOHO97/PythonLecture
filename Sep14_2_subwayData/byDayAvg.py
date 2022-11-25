# -*- coding:utf-8 -*-
from _datetime import datetime

f = open("D:/csvdict/subwayData/seoulSubway.txt", "r", encoding="utf-8")
s = f.readlines()


byDay ={}
i = None
line = None
sum = None

yoilSum = {"Sun": 0, "Mon": 0, "Tue": 0, "Wed": 0, "Thu": 0, "Fri": 0, "Sat": 0}
yoilCount = {"Sun": 0, "Mon": 0, "Tue": 0, "Wed": 0, "Thu": 0, "Fri": 0, "Sat": 0}

for i, line in enumerate(s):
    line = line.replace("\n", "").split(",")
    yoil = datetime.strftime(datetime.strptime("%s%s%s" % (line[0], line[1], line[2]), "%Y%m%d"), "%a")
    sum = int(line[5]) + int(line[6])
    yoilSum[yoil] += sum
    yoilCount[yoil] += 1
    
for k, v in yoilSum.items():
    print(k, v / yoilCount[k])
        
f.close()