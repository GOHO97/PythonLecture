# -*- coding:utf-8 -*-
import pandas as pd

# df1 = pd.read_csv("D:/csvdict/titanic.csv")
# df2 = pd.read_csv("D:/csvdict/titanic.csv")
# 
# df3 = pd.concat([df1, df2])
# print(df3)
# 
# df4 = pd.concat([df1, df2], axis=1)
# print(df4)

snack = pd.DataFrame()
snack["이름"] = ["초코파이", "새우깡"]
snack["가격"] = [5000, 2000]
snack["제조사"] = ['오리온', '농심']
print(snack)
print('-------')
company = [{'제조사': '오리온', '위치':'서울'},
           {'제조사': '농심', '위치':'부천'},
           {'제조사': '롯데', '위치':'인천'},
           {'제조사': '곰표', '위치':'대전'}]

company = pd.DataFrame(company)
#print(company)
#print('-------')

city = {"도시":["서울", '부천', '인천', '대전'],
        '인구수':[100, 50, 80, 70]}

city = pd.DataFrame(city)
#print(city)
#print('-------')

snackCompanyDF = pd.merge(snack, company, on='제조사', how="outer")
#print(snackCompanyDF)

#필드명이 다르면
companyCityDF = pd.merge(company, city, left_on="위치", right_on='도시')
#
#print(companyCityDF)
#print('-------')

#print(snack[snack["가격"] company["제조사"]] companyCityDF["도시"][companyCityDF["인구수"] == companyCityDF["인구수"].max()])

print(snack[snack["제조사"] == company[company["위치"] == (city[city['인구수'] == city['인구수'].max()]['도시'].iloc[0])]['제조사'].iloc[0]]['가격'].mean())

newDF = pd.merge(snack, company)
newDF = pd.merge(newDF, city, left_on="위치", right_on='도시')
print(newDF[newDF['인구수'] == newDF['인구수'].max()]['가격'].mean())
