import numpy as np
from sympy import *
import sympy as sp
import matplotlib.pyplot as plt

v = Function('v')
x = Function('x')
t = Symbol('t',real = True, positive = True)

a = 9.81

solution_v = dsolve(v(t).diff(t) - a, v(t), ics={v(0): 1})
solution_x = dsolve(Derivative(x(t),t,t) - a, x(t), ics={x(0): 0, sp.diff(x(t),t).subs(t,0): 1})

print("V(t) = ", solution_v)
print('X(t) =', solution_x)

t=np.linspace(0,10,200)
plt.show(t,10*t + 1, t, 5*t**2 + t)
plt.show()