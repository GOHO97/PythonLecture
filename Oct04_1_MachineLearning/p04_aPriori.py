# -*- coding:utf-8 -*-
from apyori import apriori


trainData = [['치킨', '맥주'],
             ['치킨', '피자', '맥주'],
             ['치킨', '치킨', '콜라'],
             ['피자', '소주', '맥주'],
             ['맥주', '치킨', '콜라']
             ]
result = apriori(trainData, min_support=0.5, min_confidence=0.7)
result = list(result)
for r in result:
    for r2 in r.ordered_statistics:
        print(list(r2.items_base), '을 산 사람이')
        print(list(r2.items_add), "을 살 확률이")
        print(r2.confidence)
        print("------")