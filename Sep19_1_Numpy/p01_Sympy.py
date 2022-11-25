# -*- coding:utf-8 -*-
from sympy.core.numbers import pi, Rational
from sympy.printing.pretty.pretty import pprint
import sympy
from sympy.core.symbol import symbols
from sympy.simplify.simplify import simplify
from sympy.core.function import expand, diff
from sympy.polys.polytools import factor, cancel
from sympy.core.relational import Eq
from sympy.solvers.solvers import solve
from sympy.integrals.integrals import integrate
from sympy.series.limits import limit

a = pi
print(a)
pprint(a)
pprint(sympy.N(a))

print("-----\n")

b = Rational(1, 2) # 분수
print(b)
pprint(b)

print("-----\n")

x, y = symbols("x y") # x, y를 수학식의 x, y로 쓰겠다고 선언
c = 2 * x + y ** 4 
# 2 곱하기 x 더하기 y의 4승
pprint(c)

print("-----\n")

d = 3 * x ** 5
pprint(d)
dd = d.subs(x, 2)
# subs를 통해 x의 값을 대입해서 계산
print(dd)

print("-----\n")

e = 5 * x ** 2 + 4 - 3 * y ** 3 - 10
# 상수 계산 해서 출력 해줌.
pprint(e)

ee = e.subs([[x, 1], [y, 2]])
# x에 1 y에 2 대입
print(ee)
print("------")

f = 3 * (x + 2) ** 2 + (x + 3) ** 3 + 4 * x
pprint(f)
f2 = simplify(f)
# 식 정리
pprint(f2)
f3 = "3 * 2 * (x + 3) ** 3" 
f4 = simplify(f3)
# 문자열로 된 식 정리
pprint(f4)

g = (x - 3) * (x + 5)
g2 = expand(g)
pprint(g2)

h = 2 * x ** 3 + 8
h2 = factor(h)
# 전개 반대
pprint(h2)

i = (2 * x ** 3 + 4) / (2 * x) 
pprint(i)

i2 = cancel(i)
# 약분
pprint(i2)


j = Eq(2 * x + 3, 5)
# 방정식
pprint(j)
jj = solve(j)
# 방정식 풀기
print(jj)

k1 = 2 * x + y ** 2 - 1
k2 = 3 + x ** 2 - 3 * y
kk = solve([k1, k2])
# 연립 방정식 풀기
print(kk)

l = 2 * x ** 4 + 10 * x ** 2
l2 = diff(l, x, 3)
# 미분
pprint(l2)

m = integrate(l2)
# 적분
pprint(m)

n = 2 * x - 3 + x ** 3
nn = limit(n, x, 10)
# 극한
print(nn)

