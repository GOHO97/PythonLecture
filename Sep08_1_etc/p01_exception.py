# -*- coding:utf-8 -*-

def divide(a, b):
    try:
        c = x / y
        return c
    except Exception as e:
        print(e)
        return -999
    else:
        print("예외 발생 안 하면 실행")
    finally:
        print("ㅋ")
        
x = int(input("x : "))
y = int(input("y : "))
z = divide(x, y)
print(z)

