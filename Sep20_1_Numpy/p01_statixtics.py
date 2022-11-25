# -*- coding:utf-8 -*-
import numpy as np

a = np.random.randint(1, 11, [3, 5])
print(a)

b = np.sum(a) # 총합
print(b)

c = np.mean(a) # 평균
print(c)

d = a - c
print(d)
# 각 값에서 평균을 빼서
d = d ** 2 #제곱
d = np.mean(d) # 평균
print(d)

d2 = np.var(a) # 분산
print(d2)

e = np.sqrt(d) # 제곱근
print(e)

e2 = np.std(a) #표준편차
print(e2)

# 분산, 표준편차 : 값들이  평균이랑 얼마나 떨어져있나

f = np.max(a)
print(f)

g = np.min(a)
print(g)

# 최댓값과 최솟값을 구할 때도 axis를 넣을 수 있고 0을 넣으면 열 방향 1을 넣으면 행방향에서 그 값을 찾아준다.
# 합계 같은 것 또한 동일

a2 = np.sum(a, axis=1)
print(a2)

print(a)
h = np.argmax(a) # 최댓값의 인덱스
print(h)

i = np.argmin(a) # 최솟값의 인덱스
print(i)

h2 = np.argmax(a, axis=0) # 열 방향으로 최댓값 찾기
print(h2)

j = np.cumsum(a) #누적합 오른쪽으로 계속 더해가며 나아감.
print(j)

k = np.cumprod(a) #누적곱
print(k)



