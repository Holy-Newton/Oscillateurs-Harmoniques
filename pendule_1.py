#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 11:58:35 2025

@author: francoisdeberdt
"""

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import statistics
from scipy.integrate import odeint


def pendule(Y, t, g, L, gamma):
    theta, omega = Y
    dthetadt = omega
    domegadt = -g * np.sin(theta)/L - gamma * dthetadt
    return [dthetadt, domegadt]

time = 10
Y0 = [np.pi/4, 0]

t = np.linspace(0, time, time*(20))
sol = odeint(pendule, Y0, t,args= (9.81, 1, 0.05))

plt.plot(t, sol[:, 0])
plt.show()







