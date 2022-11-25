# -*- coding:utf-8 -*-
from random import randint

userHand, comHand = None, None
handTable = [None, "가위", "바위", "보"]
win, draw, lose = 0, 0, 0

def userFire():
    global userHand, handTable
    print("가위, 바위, 보 중에 내시오")
    userHand = input("뭐 낼겨? : ")
    if userHand != "가위" and userHand != "바위" and userHand != "보":
        print("잘못 냈음 다시 내셈")
        print("--------------")        
        userFire()
    else:
        userHand = handTable.index(userHand)

def comFire():
    global comHand
    comHand = randint(1, 3)

def printHand():
    global userHand, comHand, handTable
    print("유저 : ", handTable[userHand])
    print("컴 : ", handTable[comHand])
    
def judge():
    global userHand, comHand, win, draw, lose
    t = userHand - comHand
    if t == 0:
        print("무")
        draw += 1
    elif t == -1 or t == 2:
        print("패")
        lose += 1
    else:
        print("승")
        win += 1
    print("------------")
def printResult():
    global win, draw, lose
    print("승 : %d번, 패 : %d번, 무 : %d번" % (win, lose, draw))

for i in range(5):
    userFire()
    comFire()
    printHand()
    judge()
printResult()

    