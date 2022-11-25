# -*- coding:utf-8 -*-
import pandas as pd

df = pd.read_csv("D:/csvdict/sherlockResult.txt", sep="\t", names=["word", "count"])
df = df.sort_values(by=["count", "word"], ascending=[False, True])
print(df)

print(df.head(30))
