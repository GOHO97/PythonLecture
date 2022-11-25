# -*- coding:utf-8 -*-
import numpy as np

f = open("D:/jejuWeather/totalJejuWeather.txt", "r", encoding="utf-8")

line = None
tempSum = {}
tempCount = {}

for line in f.readlines():
    line = line.replace("\n", "").split(",")
    if line[2] in tempSum :
        tempSum[line[2]] += float(line[3])
        tempCount[line[2]] += 1
    else:
        tempSum[line[2]] = float(line[3])
        tempCount[line[2]] = 1
f.close()

time = []
tempavg = []

for k, v in tempCount.items():
    time.append(k)
    tempavg.append(tempSum[k] / v)

time = np.array(time)
tempavg = np.array(tempavg)

#print(time[np.argmax(tempavg)])
#print(time[np.argmin(tempavg)])
#minTemp = np.min(tempavg)
#print(minTemp)
#print(time[tempavg == minTemp], tempavg[tempavg == minTemp])
sumAvgTemp = np.mean(tempavg)
print(sumAvgTemp)
time2 = time[tempavg > sumAvgTemp]
temp2 = tempavg[tempavg > sumAvgTemp]
for i in range(time2.size):
    print(time2[i], temp2[i])
    print(type(time2))