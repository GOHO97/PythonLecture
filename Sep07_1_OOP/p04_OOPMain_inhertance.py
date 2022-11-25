# -*- coding:utf-8 -*-

class Avengers:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def attack(self):
        print("공격")
    
    def eat(self):
        print("전투식량 냠")
        
class Ironman(Avengers):
    def attack(self):
        Avengers.attack(self)
        print("빔 발사")

class Hulk(Avengers):
    
    def __init__(self, name, age, pantsSize):
        Avengers.__init__(self, name, age)
        self.pantsSize = pantsSize

class Human:
    def eat(self):
        print("냠")
        
  
class Spiderman(Avengers, Human):  
    
    def eat(self):
        #super().eat() #앞에 쓴거
        Human.eat(self)
        Avengers.eat(self)


s = Spiderman("파커", 20)
s.attack()
s.eat()



