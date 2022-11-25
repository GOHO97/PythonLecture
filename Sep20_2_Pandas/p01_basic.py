# -*- coding:utf-8 -*-
import pandas as pd

a = pd.Series([123, 4, 234])
#print(a)
#print(a[0])

b = pd.DataFrame()
b["이름"] = ["새우깡", "양파링", "포카칩"]
b["가격"] = [3000, 5000, 6000]
print(b)

print(b["이름"])

b = b.set_index(b["이름"])
print(b)
#print(b.iloc[1])
print(b.loc["새우깡"])