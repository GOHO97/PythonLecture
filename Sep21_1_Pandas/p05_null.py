# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

md = pd.read_csv("D:/csvdict/marketData/price.csv", names=["시장 이름", "상품 이름", "가격", "시장 유형", "구 이름"])

md["상품 이름"] = md["상품 이름"].fillna("없음")
print(md[md["상품 이름"].str.contains("사과")][["시장 이름", "상품 이름"]])

md["상품 이름"] = md["상품 이름"].replace("없음", np.nan)
print(md[md["상품 이름"].isnull()])