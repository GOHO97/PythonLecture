# -*- coding:utf-8 -*-

f = open("D:/vsc/KakaoTalkChats.txt", "r", encoding="utf-8")

taltTxtLines = f.readlines()

msg = None
keword = None
msgdict = {}


for i, line in enumerate(taltTxtLines):
    if i > 4:
        line = line.replace("\n", "")
        msg = None
        if not line.startswith("2022년") and line != "":
            msg = line
        else:
            try:
                msg = line.split(" : ")[1]
            except:
                pass
        if msg != None:
            msg = msg.split(" ")
            for word in msg:
                if word in msgdict:
                    msgdict[word] += 1
                else:
                    msgdict[word] = 1


sendTextFile = open("D:/vsc/keyword.txt", "a", encoding="utf-8")

for k, v in msgdict.items():
    sendTextFile.write("%s\t%d\n" % (k, v))

sendTextFile.close() 
f.close()


