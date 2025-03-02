#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 13:14:55 2025

@author: francoisdeberdt
"""

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import statistics
from scipy.integrate import odeint



g, l = 9.81 , 1




def f(y,t):
    theta, omega = y
    dtheta = omega
    domega = (-g/l)* np.sin(theta)
    return [dtheta, domega]

y0 = [np.pi/4, 0]
t = np.linspace(0, 10, 500)
sol = odeint(f, y0, t)

plt.plot(t, sol[:,0])
plt.show()