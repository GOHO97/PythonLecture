# -*- coding:utf-8 -*-
import pandas as pd

df = pd.read_csv("D:/csvdict/titanic.csv")

df["Age"] = df["Age"].fillna(200)
df["Age"] = df["Age"].apply(lambda age:"%d0대" % (age // 10))
df["Age"] = df["Age"].replace("200대", "추정불가") 
                            
print(df.groupby(["Age", "Survived"])["PassengerId"].count())