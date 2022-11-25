# -*- coding:utf-8 -*-
# 결과 파일 열어서 한줄 씩 출력
# 언급 횟수순 내림차순 정렬

class Word:
    
    def __init__(self, line):
        line = line.replace("\n", "").split("\t")
        self.word = line[0]
        self.count = int(line[1])
        
    def printInfo(self):
        print(self.word, self.count)

        
f = open("D:/vsc/keyword.txt", "r", encoding="utf-8")

words = []
for line in f.readlines():
    words.append(Word(line))

words.sort(key=(lambda w:w.word), reverse=False)
for w in words:
    w.printInfo()
    
f.close()
