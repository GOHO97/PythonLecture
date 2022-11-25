# -*- coding:utf-8 -*-

class deepRacer:
    def __init__(self, color, battery):
        self.color = color
        self.battery = battery
    
    def printInfo(self):
        print(self.color)
        print(self.battery)
 
if __name__ == "__main__":       
    from animal.pet import cat
    c = cat("고영희", "3")
    c.printInfo()