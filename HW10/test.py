# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 16:10:53 2019

@author: Nate
"""

import numpy as np
import matplotlib.pyplot as plt
import pdb

n = []
for i in range(int(2e5)):
    n.append(np.random.randn())


fig1, axes1 = plt.subplots()

axes1.hist(n*5, 1000)
axes1.hist(n, 1000)

axes1.set_ylabel('Energy')
axes1.set_xlabel('alpha')
axes1.set_title("Energy vs alpha", va='bottom')


plt.show()