# -*- coding:utf-8 -*-

s = input("뭐 : ")
# 무언가를 입력 받고
f = open("D:/vsc/0908.txt", "a", encoding="utf-8")
# 폴더를 연다. 있는건 열고 없는걸 만들어주진 않는다. 파일은 만들어준다.
# 앞의 자리는 파일 경로를 써주고 어떤 mode인지를 써주는데
# r : read, w : write, a : append(파일 뒤에 뭐가 추가 되도록 하는 것)

f.write(s + "\n")
f.close()