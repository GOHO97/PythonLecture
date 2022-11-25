# -*- coding:utf-8 -*-
import pandas as pd

md = pd.read_csv("D:/csvdict/marketData/price.csv", names=["시장 이름", "상품 이름", "가격", "시장 유형", "구 이름"])
# 시장이름으로 정렬
md = md.set_index(md["시장 이름"])
md = md.sort_index()
# 통인시장 것만
print(md.loc["통인시장"])
# 농협 것만
print(md[md["시장 이름"].str.contains("농협")])
# 품명 가나다 -> 가격 내림차순
print(md.sort_values(by = ['상품 이름', '가격'], ascending=[True, False]))
# 사과를 살려면 어디로 가야[시장명]
print(md.loc[md[md["상품이름"] != NA & md["상품 이름"] != NaN & md["상품 이름"].str.contains("사과")]])
# 강남구 데이터만 반복문 써서 출력

