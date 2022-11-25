# -*- coding:utf-8 -*-
from sympy.simplify.simplify import simplify
from sympy.core.function import diff
from sympy.printing.pretty.pretty import pprint
from sympy.core.symbol import symbols

x = symbols("x")
sick = simplify(input("식 입력 : "))
count = int(input("미분 할 횟 수 : "))
ab = diff(sick, x, count)
pprint(ab)
no = float(input("x값 : "))
ans = sick.subs(x, no)
print(ans)
