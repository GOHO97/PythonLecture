# -*- coding:utf-8 -*-
import numpy as np

f = open("D:/csvdict/subwayData/seoulSubway.txt", "r", encoding="utf-8")

data = None
ride = {}
alight = {}

for data in f.readlines():
    data = data.replace("\n", "").split(",")
    if data[4] in ride :
        ride[data[4]] += int(data[5])
        alight[data[4]] += int(data[6])
    else:
        ride[data[4]] = int(data[5])
        alight[data[4]] = int(data[6])
    
f.close()

k, v = None, None
namelist, ridelist, alightlist = [], [], []

for k, v in ride.items():
    namelist.append(k)
    ridelist.append(v)
    alightlist.append(alight[k])
   
nameNpArray = np.array(namelist)
rideNpArray = np.array(ridelist)
alightNpArray = np.array(alightlist)
ans = nameNpArray[rideNpArray < alightNpArray]
print(ans)
print(len(ans))

