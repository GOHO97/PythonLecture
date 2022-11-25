# -*- coding:utf-8 -*-
import pandas as pd

df = pd.read_csv("D:/csvdict/titanic.csv")
df = df.set_index(df["Name"])
print(df)
print('---------')

df = df.sort_index()
print(df)

df = df.sort_index(ascending = False)
print(df)

df = df.sort_index(axis=1)
print(df)

df = df.sort_values(by="Pclass")
print(df[["Name", 'Pclass']])

df = df.sort_values(by=["Pclass", 'Age'], ascending=[False, True])
print(df[['Name', 'Pclass', 'Age']])

for i in df.index:
    print(df.loc[i])
    
    