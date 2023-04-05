# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 14:48:04 2023

@author: Mehmet Akif ERDAS
"""
import math

import matplotlib.pyplot as plt

yuks = 1.5 # metre cinsi yukseklik
uzak = 0
V_int = 112.64 #ilk hiz - curve fitting ile bulundu baska bir dosyada zipe eklendi.
a_sx = 0 #yataydaki ivme
t_sure = 0 # zaman modeli
t= 0.01 # zaman intervali
A_r = 0.0000287433
V_sx = V_int - (a_sx * t) #yataydaki hiz
ro_hava = 1.228 #kg/m3 havanin yogunlugu
m = 0.00026 #kg cinsinden mermi agirlik
g= 9.814 #gravity
c_d = 0.5142
V_sy = 0 #baslangictaki dusey hiz
F_dy = 0.5 * ro_hava * c_d * A_r * V_sy * V_sy #x ekseninde hava direnci
sayac =0

uzak_list = []
V_list = []

while yuks >= 0 :
    F_dx = 0.5 * ro_hava * c_d * A_r * V_sx * V_sx #x ekseninde hava direnci
    a_sx = F_dx / m # x eksenindeki ivme
    V_sx = V_sx - (a_sx * t) #yataydaki hiz
    uzak = uzak + V_sx*t
    
    
    
    
    F_ty = m*g - F_dy
    a_sy = F_ty/m
    V_sy = V_sy + (a_sy * t) #yataydaki hiz
    F_dy = 0.5 * ro_hava * c_d * A_r * V_sy * V_sy #x ekseninde hava direnci
    
    yuks = yuks - V_sy*t #dusme modeli
    
    euler = math.atan(F_dy/F_dx) #euler açısı
    
    V_abs = math.sqrt((V_sy*V_sy) + (V_sx*V_sx))
    
    V_list.append(V_abs)
    uzak_list.append(uzak)
    
    
    
    
    sayac += 1
    t_sure = t_sure + t
    
print(t_sure)
#print(V_list)


plt.figure()

velocity=[108.83, 88.84, 76.41, 64.27] #verilen dataların ortalaması
distence=[1, 6, 11, 16]

plt.plot(distence,velocity,'bo',label='verilenler')

plt.plot(uzak_list, V_list, 'r-')
plt.show()


    
    