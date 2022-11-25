# -*- coding:utf-8 -*-
import pandas as pd

md = pd.read_csv("D:/csvdict/marketData/price.csv", names=["시장명", "상품명", "가격", "분류", "구"])
#print(md['가격'].mean())
#print(md.groupby("분류")['가격'].mean())
print(md.groupby(["구", "분류"])['가격'].mean())

#기상청 날씨, 날시별 평균기온