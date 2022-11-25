# -*- coding:utf-8 -*-

class snack():
   
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __del__(self):
        print("과자가 사라짐")
        
    def printInfo(self):
        print(self.name)
        print(self.price)


s = snack("새우깡", 5000)
s.printInfo()

s2 = snack("빼빼로", 1000)
s2.printInfo()

s3 = s
s3.printInfo()

s = None
s2 = None
s3 = None

print("끝")