# -*- coding:utf-8 -*-
import pandas as pd

df = pd.read_csv("D:/csvdict/part-r-00000", sep="\t", names=['글자', '횟수'])

df = df.sort_values(by=["횟수", "글자"], ascending=[False, True])
print(df.head(30))