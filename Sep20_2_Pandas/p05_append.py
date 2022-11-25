# -*- coding:utf-8 -*-
import pandas as pd

a = pd.DataFrame()
a['이름'] = ['새콤달콤', '빼뺴로']
a['가격'] = [500, 1500]
print(a)
print("-----")

b = pd.Series(['새우깡', 3000], index=["이름", '가격'])
a = a.append(b, ignore_index=True) # Series가 이용하던 index 체계를 무시하라는 뜻
print(a)

c = {'이름': '츄파춥스', '가격': 300}
a = a.append(c, ignore_index=True)
print(a)
