# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 14:48:04 2023

@author: Mehmet Akif ERDAS
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
velocity=[108.83, 88.84, 76.41, 64.27] #verilen dataların ortalaması
distence=[1, 6, 11, 16]

plt.plot(distence,velocity,'ro',label='verilenler')

p = np.polyfit(distence,velocity,2)

xfit=np.linspace(0,max(distence), 1000)
yfit=np.polyval(p, xfit)
plt.plot(xfit,yfit,color='blue',label='Best Fit - egrimiz')

print(yfit)
plt.legend()
plt.show()

"""
Burada öncelikle veriyi programa verip datayı fitledik.
sonrasında yfit kısmındaki verileri bastırıp en üstteki veriyi çekerek initial velocityi bulduk.
"""
