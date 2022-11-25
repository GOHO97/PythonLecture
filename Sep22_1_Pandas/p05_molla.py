# -*- coding:utf-8 -*-
import pandas as pd

df = pd.read_csv("D:/csvdict/individualService/data.csv", names=["업종", "주소", "품목", "가격"])

#업종별 평균가
df = df[df['가격'] > 0]
print(df.groupby("업종")["가격"].mean())

df["주소"] = df["주소"].fillna("주소 없음")

def getGu(a):
    a = a.split(" ")
    if a[0].endswith("구"):
        return a[0]
    else:
        return a[1]
    
df["구명"] = df["주소"].apply(getGu)

# 구별 평균가
print(df.groupby("구명")["가격"].mean())

# 구별, 항목별 평균가
print(df.groupby(["구명", "품목"])["가격"].mean())

# 업종별, 구별 평균가
print(df.groupby(["업종", "구명"])["가격"].mean())