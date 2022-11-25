# -*- coding:utf-8 -*-

a = ['a', 'b', 'c']
b = ['d', 'a', 'b', 'e']
for bb in b:
    if bb in a:
        print(bb)
        # 리스트 속에 있나 없나를 in으로 체크 가능
        
print("----")
c = []
for bb in b:
    c.append(bb)
print(c)
# b에 있는거 c로 넣어줌.

c2 = [bb for bb in b]
print(c2)
# 근데 이런 것도 있다 위랑 똑같다.

# d에다가 b에 있는 것 중에 a에는 없는 것만
d = []
for bb in b:
    if bb not in a:
        d.append(bb)

# 저 c2의 신기한 방법을 따라 쓰자면
d = [bb for bb in b if bb not in a]
# 조건문을 뒤에 써주면 됨.


