# -*- coding:utf-8 -*-
import pandas as pd
from cx_Oracle import connect

# 첫 줄이 필드명이라 자동 처리 됨.
#a = pd.read_csv("D:/csvdict/titanic.csv")
#print(a)

# 첫 줄이 제목 없이 바로 데이터면 제목을 넣어줘야 함.
#b = pd.read_csv("D:/csvdict/subwayData/seoulSubway.txt", names=["년", "월", '일', '노선', '역', '승차자', '하차자'])
#print(b)

# txt(\t로 구분해놓은, 제목 없고)
# .csv, .txt, ... : 확장자는 윈도우에만 있는 허상, 단지 사람이 보기에 편하게 하기 위하여있는 개념
#c = pd.read_csv("D:/csvdict/naverMovie.txt", sep="\t", names=['월', '일', '시', '제목', '평점', '리뷰'])
#print(c)

con = connect("sleep/1@sdgn-djvemfu.tplinkdns.com:19195/xe")
sql = "select * from owm_weather_kwon"
d = pd.read_sql(sql, con)
print(d)
con.close()


