# -*- coding:utf-8 -*-

class cat:
    '''
        클래스 설명서
    '''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def printInfo(self):
        '''
                메소드 설명서
        '''
        print(self.name, self.age)
        
        
class dog:
    pass

help(cat)
help(print)

if __name__ == "__main__":
    from transportation.car import deepRacer
    dr = deepRacer("검은색", "30")
    dr.printInfo()