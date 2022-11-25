# -*- coding:utf-8 -*-
import pandas as pd

subwayDF = pd.read_csv('D:/csvdict/subwayData/seoulSubway.txt', names=['년', '월', '일', '노선', '역', '승차자', '하차자'])
# 필드명 출력
#print(subwayDF.columns)
# 마지막 10개
#print(subwayDF.tail(10))
# 첫 3개 날짜
#print(subwayDF.head(3).head([["년", '월', '일']]))
# 10 ~ 15번 데이터의 노선, 역
#print(subwayDF.iloc[10:16][["노선", '역']])
# 3호선 역, 탄, 내린 사람 조회

# 인덱스 노선으로 지정
# subwayDF = subwayDF.set_index(subwayDF["노선"])
# 2호선 전체 조회
#print(subwayDF.loc["2호선"])
# 3호선 역, 탄, 내린 사람 조회
#print(subwayDF.loc["3호선",['역', '승차자', '하차자']])
#subwayDF = subwayDF.set_index(subwayDF["승차자"])
#print(subwayDF[subwayDF['승차자'] > 50000])
#print(subwayDF[subwayDF['승차자'] < 100][['년', '월', '일', '노선', '역']])

#print(subwayDF[subwayDF["역"].str.contains("입구")])
print(subwayDF[subwayDF["역"].str.startswith("서울")]['노선'])