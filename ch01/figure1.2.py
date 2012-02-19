#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

N = 10
SCALE = 0.3

x = np.linspace(0, 1, N)
t = np.sin(2 * np.pi * x) + np.random.normal(0, SCALE, x.size)
plt.plot(x, t, 'bo')

curve_x = np.linspace(0, 1, 100)
curve_t = np.sin(2 * np.pi * curve_x)
plt.plot(curve_x, curve_t, 'g-')

plt.xlabel('$x$')
plt.ylabel('$t$')
plt.axis([-0.05, 1.05, -1.5, 1.5])
plt.savefig('figure1.2.png')
