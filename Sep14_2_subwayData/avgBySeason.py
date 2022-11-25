# -*- coding:utf-8 -*-

f = open("D:/csvdict/subwayData/seoulSubway.txt", "r", encoding="utf-8")
s = f.readlines()
i = None
line = None
sum = None

seasonSum = {"Spring": 0, "Summer": 0, "Autumn": 0, "Winter": 0}
seasonCount = {"Spring": 0, "Summer": 0, "Autumn": 0, "Winter": 0}
seasons = [None, "Winter", "Winter", "Spring", "Spring", "Spring", "Summer", "Summer", "Summer", "Autumn", "Autumn", "Autumn", "Winter"]
for i, line in enumerate(s):
    line = line.replace("\n", "").split(",")
    season = seasons[int(line[1])]
    sum = int(line[5]) + int(line[6])
    seasonSum[season] += sum
    seasonCount[season] += 1
    
for k, v in seasonSum.items():
    print(k, v / seasonCount[k])
        
f.close()