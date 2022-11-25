# -*- coding:utf-8 -*-
import pandas as pd

df = pd.read_csv("D:/csvdict/busData/busCSV2015.txt", names=["년", '월', '일', '노선', '정류장', '승차자', '하차자'])
df = df.head(5000)
print(df)