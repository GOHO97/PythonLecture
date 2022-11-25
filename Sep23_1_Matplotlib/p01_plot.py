# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fontFile = "C:/Windows/Fonts/malgun.ttf"
# 설치된 폰트파일 경로
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
# 폰트명
plt.rc("font", family=fontName)

yData = np.array([10, 20, 17, 40, 50])
xData = [10, 20, 30, 40, 50]

# 기본
# 
# plt.xlabel('x축')
# plt.ylabel('y축')
# 
# plt.axis([0, 100, 1, 200])
# x최소, x최대, y최소, y최대



#d = {"fontsize": 20, "fontweight":'bold', 'color': "#FF0000"} # bold, ultrabold, light, hltralight 도 있다.
# plt.title("왼쪽제목", loc="left")
# plt.title("오른쪽제목", loc="right")
# plt.title("중간제목", loc="center", fontdict=d)




#plt.plot(xData, yData, color="#43A047", linestyle=":", marker="+", linewidth=5, markersize=10)
#plt.grid(axis="y")


# plt.xticks(xData, ['십', '이십사', '삼십', '사십구', '십이', '백팔'])
# plt.yticks(np.arange(0, 31, 10), ['ㄷ', 'ㄹ', 'ㅁ', 'ㅂ'])
# plt.tick_params("y", direction='in', length=20, pad=30)
# plt.tick_params("x", labelsize=20, labelcolor="#33FFFF")



yData2 = [100, 300, 150, 200, 220]
_, subplot1Conf = plt.subplots()
p1 = subplot1Conf.plot(xData, yData, color="red")
subplot1Conf.set_xlabel("엑스")
subplot1Conf.set_ylabel("와이1")

subplot2Conf = subplot1Conf.twinx()
p2 = subplot2Conf.plot(xData, yData2, "g--")
subplot2Conf.set_ylabel("와이2")

subplot1Conf.legend(["빨간거", "초록색"])

plt.show()

