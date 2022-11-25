# -*- coding:utf-8 -*-
import pandas as pd

md = pd.read_csv("D:/csvdict/marketData/price.csv", names=["시장 이름", "상품 이름", "가격", "시장 유형", "구 이름"])
md["시장 유형"] = md["시장 유형"].replace('대형마트', '마트')
print(md)

# 마트 -> 일요일에 노는 곳, 전통시장 -> 일요일도 하는 곳으로 수정
#md["시장 유형"] = md["시장 유형"].replace(["마트", '전통시장'], ['일요일에 노는 곳', '일요일도 하는 곳'])
#print(md)
# 노는 곳 -> 마트, 하는 곳 -> 시장 2탄
#md["시장 유형"] = md["시장 유형"].replace({"일요일에 노는 곳": "마트", '일요일도 하는 곳': '전통시장'})
#마트/시장 -> 돈 쓰는 곳
#md["시장 유형"] = md["시장 유형"].replace(["마트", "시장"], "돈 쓰는 곳")  
md = md.rename(columns={"시장 이름": '시장명', "상품 이름": "상품명"})
print(md)