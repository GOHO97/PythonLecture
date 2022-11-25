# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

df = pd.read_csv("D:/csvdict/mosquitoData/mosquito.csv", names=['날짜', '수변부', '주거지', '공원'])

df['수변부'] = df['수변부'].replace("None", np.nan)
df['주거지'] = df['주거지'].replace("None", np.nan)
df['공원'] = df['공원'].replace("None", np.nan)

df['수변부'] = pd.to_numeric(df['수변부'])
df['주거지'] = pd.to_numeric(df['주거지'])
df['공원'] = pd.to_numeric(df['공원'])

df['수변부'] = df['수변부'].fillna(df['수변부'].mean())
df['주거지'] = df['주거지'].fillna(df['주거지'].mean())
df['공원'] = df['공원'].fillna(df['공원'].mean())

df['평균'] = (df['수변부'] + df['주거지'] + df['공원']) / 3

print(df[df['평균'] == df['평균'].max()])
